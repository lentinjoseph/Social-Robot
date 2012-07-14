// Cristóbal Carnero Liñán <grendel.ccl@gmail.com>
//
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 #if (defined(_WIN32) || defined(__WIN32__) || defined(__TOS_WIN__) || defined(__WINDOWS__) || (defined(__APPLE__) & defined(__MACH__)))
#include <cv.h>
#include <highgui.h>
#else
#include <cv.h>
#include <highgui.h>
#endif

#include "cvblob.h"
using namespace cvb;
size_t count1;
 FILE *fp;
 void file(const char *text)

	{
	fp = fopen("sample.txt", "w");
    	if(fp == NULL) {
        	perror("failed to open sample.txt");
        	//return EXIT_FAILURE;
    }
    count1 = fwrite(text, strlen(text), 1, fp);
    printf("Wrote %u bytes. fclose(fp) %s.\n", count1, fclose(fp) == 0 ? "succeeded" : "failed");
    //return EXIT_SUCCESS;
    //system("python move.py");
    system("python tcpclient.py");
}


int main()
{
  CvTracks tracks;
  CvTracks tracksl;
  int count=0;
  int love=0;
  double centx=0;
  double centy=0;
  int x,y=0; 
 //   void file(char *text);
  // char *str = "hello\n";

  cvNamedWindow("red_object_tracking=blue", CV_WINDOW_AUTOSIZE);
  cvNamedWindow("red_object_tracking=red", CV_WINDOW_AUTOSIZE);
  CvCapture *capture = cvCaptureFromCAM(0);
  cvGrabFrame(capture);
  IplImage *img = cvRetrieveFrame(capture);

  CvSize imgSize = cvGetSize(img);

  IplImage *frame = cvCreateImage(imgSize, img->depth, img->nChannels);
  IplImage *framel = cvCreateImage(imgSize, img->depth, img->nChannels);
  IplConvKernel* morphKernel = cvCreateStructuringElementEx(5, 5, 1, 1, CV_SHAPE_RECT, NULL);

  //unsigned int frameNumber = 0;
  unsigned int blobNumber = 0;
 
  bool quit = false;
  while (!quit&&cvGrabFrame(capture))
  {
    IplImage *img = cvRetrieveFrame(capture);

    cvConvertScale(img, frame, 1, 0);
    cvConvertScale(img, framel, 1, 0);
    IplImage *segmentated = cvCreateImage(imgSize, 8, 1);
    IplImage *segmentatedl = cvCreateImage(imgSize, 8, 1);
    // Detecting red pixels:
    // (This is very slow, use direct access better...)
    for (unsigned int j=0; j<imgSize.height; j++)
      for (unsigned int i=0; i<imgSize.width; i++)
      {
	CvScalar c = cvGet2D(frame, j, i);

	double b = ((double)c.val[0])/255.;
	double g = ((double)c.val[1])/255.;
	double r = ((double)c.val[2])/255.;
	unsigned char f = 255*((b>0.2+r)&&(b>0.2+g));

	cvSet2D(segmentated, j, i, CV_RGB(f, f, f));
      }
	//Detecting blue pixels

	for (unsigned int j=0; j<imgSize.height; j++)
      for (unsigned int i=0; i<imgSize.width; i++)
      {
	CvScalar d = cvGet2D(frame, j, i);

	double bl = ((double)d.val[0])/255.;
	double gl = ((double)d.val[1])/255.;
	double rl = ((double)d.val[2])/255.;
	unsigned char fl = 255*((rl>0.2+gl)&&(rl>0.2+bl));

	cvSet2D(segmentatedl, j, i, CV_RGB(fl, fl, fl));
	      
	}

    cvMorphologyEx(segmentated, segmentated, NULL, morphKernel, CV_MOP_OPEN, 1);
    cvMorphologyEx(segmentatedl, segmentatedl, NULL, morphKernel, CV_MOP_OPEN, 1);
  //  cvShowImage("segmentated", segmentated);
  //  cvShowImage("segmentatedl", segmentatedl);
    IplImage *labelImg = cvCreateImage(cvGetSize(frame), IPL_DEPTH_LABEL, 1);
    IplImage *labelImgl = cvCreateImage(cvGetSize(framel), IPL_DEPTH_LABEL, 1);
    CvBlobs blobs;
    CvBlobs blobsl;
    unsigned int result = cvLabel(segmentated, labelImg, blobs);
    unsigned int resultl = cvLabel(segmentatedl, labelImgl, blobsl);
    cvFilterByArea(blobs, 500, 1000000);
        cvFilterByArea(blobsl, 500, 1000000);
    cvRenderBlobs(labelImg, blobs, frame, frame,CV_BLOB_RENDER_CENTROID|CV_BLOB_RENDER_BOUNDING_BOX);
  cvRenderBlobs(labelImgl, blobsl, framel, framel,CV_BLOB_RENDER_CENTROID|CV_BLOB_RENDER_BOUNDING_BOX);
    cvUpdateTracks(blobs, tracks, 200., 5);
    cvUpdateTracks(blobsl, tracksl, 200., 5); 
   cvRenderTracks(tracks, frame, frame, CV_TRACK_RENDER_ID|CV_TRACK_RENDER_BOUNDING_BOX); //   CV_TRACK_RENDER_TO_LOG);
  cvRenderTracks(tracksl, framel, framel, CV_TRACK_RENDER_ID|CV_TRACK_RENDER_BOUNDING_BOX);//|CV_TRACK_RENDER_TO_LOG);
//    printf("%s",CV_TRACK_RENDER_TO_LOG);




//FINDING THE CORDINATES AND TAKE DICISION ACCORDING TO POSITION


     for (CvBlobs::const_iterator it=blobs.begin(); it!=blobs.end(); ++it)
{
 std:: cout << ": Area1=" << it->second->area << std::endl;
	centx=it->second->centroid.x;
	centy=it->second->centroid.y;

	x=centx;
	y=centy;


 count++;
if(count==10){
	
	

	 printf("Blob1 centroid=%lf\t %lf\n",centx,centy);
	

	// LEFT
	if(x < 60 && y < 200)
	{
	printf("BOTTOM LEFT UP\n");
	file("LEFT UP");
	}
	else if((x < 60) &&  ((y < 280) && (y > 200)))
	{
	printf("BOTTOM LEFT\n");
	file("LEFT\n");
	}
	else if((x < 60) && ((y < 480) && (y > 280)))
	{
	printf("BOTTOM LEFT DOWN\n");
	file("LEFT DOWN\n");
	}
	

	//RIGHT

	else if((x > 580) &&  (y < 200))
	{
	printf("BOTTOM RIGHT UP\n");
	file("RIGHT UP\n");
	}
	else if((x > 580) && ((y < 280) && (y > 200)))
	{
	printf("BOTTOM RIGHT\n");
	file("RIGHT\n");
	}
	else if((x > 580) && (y > 280))
	{
	printf("BOTTOM RIGHT DOWN\n");
	file("RIGHT DOWN\n");
	}
	


	//EYELEFT

	else if(((x < 280) && (x > 60)) && (y < 200))
	{
	printf("EYE LEFT EYE APP UP\n");
	file("ILAPPUP\n");
	}
	else if(((x < 280) && (x > 60)) && ((y < 280) && (y > 200)))
	{
	printf("EYE LEFT EYE APP MID\n");
	file("ILAPPMID\n");
	}
	else if(((x < 280) && (x > 60)) && ((y < 480) && (y > 280)))
	{
	printf("EYE LEFT EYE APP DOWN\n");
	file("ILAPPDWN\n");
	}
	

	//EYE RIGHT

	else if(((x < 580) && (x > 360)) && (y < 200))
	{
	printf("EYE RIGHT EYE APP UP\n");
	file("IRAPPUP\n");
	}
	
	else if(((x < 580) && (x > 360)) && ((y < 280) && (y > 200)))
	{
	printf("EYE RIGHT EYE APP MID\n");
	file("IRAPPMID\n");
	}
	else if(((x < 580) && (x > 360)) && ((y < 480) && (y > 280)))
	{
	printf("EYE RIGHT EYE APP DOWN\n");
	file("IRAPPDWN\n");
	}
	
	//MIDDLE

	else if(((x < 360) && (x > 280)) && (y < 200))
	{
	printf("EYE MID EYE APP UP\n");
	file("IMIDAPPUP\n");
	}
	else if(((x < 360) && (x > 280)) && ((y < 280) && (y > 200)))
	{
	printf("EYE MID EYE APP MID\n");
	file("IMIDAPPMID\n");
	}
	else if(((x < 360) && (x > 280)) && (y > 280))
	{
	printf("EYE MID EYE APP DOWN\n");
	file("IMIDAPPDWN\n");
	}
	
	//printf("i found a blue object\n");
	//file("blue\n");
	count=0;	
 	
	
}
	
	
}
	




for (CvBlobs::const_iterator it=blobsl.begin(); it!=blobsl.end(); ++it)
{
  
	 //std:: cout << ": Area1=" << it->second->area << std::endl;	
	centx=it->second->centroid.x;
	centy=it->second->centroid.y;
	if((it->second->area > 40000) && (it->second->area < 80000))
		love++;
		if(love > 10)
		{
			file("love\n");
			love=0;
		}

	x=centx;
	y=centy;


 count++;
if(count==10){
	
	

	 printf("Blob1 centroid=%lf\t %lf\n",centx,centy);
	

	// LEFT
	if(x < 60 && y < 200)
	{
	printf("BOTTOM LEFT UP\n");
	file("BOTLUP\n");
	}
	else if((x < 60) &&  ((y < 280) && (y > 200)))
	{
	printf("BOTTOM LEFT\n");
	file("BOTL\n");
	}
	else if((x < 60) && ((y < 480) && (y > 280)))
	{
	printf("BOTTOM LEFT DOWN\n");
	file("BOTLDWN\n");
	}
	

	//RIGHT

	else if((x > 580) &&  (y < 200))
	{
	printf("BOTTOM RIGHT UP\n");
	file("BOTRUP\n");
	}
	else if((x > 580) && ((y < 280) && (y > 200)))
	{
	printf("BOTTOM RIGHT\n");
	file("BOTR\n");
	}
	else if((x > 580) && (y > 280))
	{
	printf("BOTTOM RIGHT DOWN\n");
	file("BOTRDWN\n");
	}
	


	//EYELEFT

	else if(((x < 280) && (x > 60)) && (y < 200))
	{
	printf("EYE LEFT EYE APP UP\n");
	file("ILAPPUP\n");
	}
	else if(((x < 280) && (x > 60)) && ((y < 280) && (y > 200)))
	{
	printf("EYE LEFT EYE APP MID\n");
	file("ILAPPMID\n");
	}
	else if(((x < 280) && (x > 60)) && ((y < 480) && (y > 280)))
	{
	printf("EYE LEFT EYE APP DOWN\n");
	file("ILAPPDWN\n");
	}
	

	//EYE RIGHT

	else if(((x < 580) && (x > 360)) && (y < 200))
	{
	printf("EYE RIGHT EYE APP UP\n");
	file("IRAPPUP\n");
	}
	
	else if(((x < 580) && (x > 360)) && ((y < 280) && (y > 200)))
	{
	printf("EYE RIGHT EYE APP MID\n");
	file("IRAPPMID\n");
	}
	else if(((x < 580) && (x > 360)) && ((y < 480) && (y > 280)))
	{
	printf("EYE RIGHT EYE APP DOWN\n");
	file("IRAPPDWN\n");
	}
	
	//MIDDLE

	else if(((x < 360) && (x > 280)) && (y < 200))
	{
	printf("EYE MID EYE APP UP\n");
	file("IMIDAPPUP\n");
	}
	else if(((x < 360) && (x > 280)) && ((y < 280) && (y > 200)))
	{
	printf("EYE MID EYE APP MID\n");
	file("IMIDAPPMID\n");
	}
	else if(((x < 360) && (x > 280)) && (y > 280))
	{
	printf("EYE MID EYE APP DOWN\n");
	file("IMIDAPPDWN\n");
	}
	//printf("i found a red object\n");
	//file("red\n");
	count=0;	
 	
	
}














}

    cvShowImage("red_object_tracking=blue", frame);
    cvShowImage("red_object_tracking=red", framel);

    /*std::stringstream filename;
    filename << "redobject_" << std::setw(5) << std::setfill('0') << frameNumber << ".png";
    cvSaveImage(filename.str().c_str(), frame);*/

    cvReleaseImage(&labelImg);
    cvReleaseImage(&labelImgl);
    cvReleaseImage(&segmentated);
    cvReleaseImage(&segmentatedl);

    char k = cvWaitKey(10)&0xff;
    switch (k)
    {
      case 27:
      case 'q':
      case 'Q':
        quit = true;
        break;
      case 's':
      case 'S':
  /*      for (CvBlobs::const_iterator it=blobs.begin(); it!=blobs.end(); ++it)
        {
          std::stringstream filename;
          filename << "redobject_blob_" << std::setw(5) << std::setfill('0') << blobNumber << ".png";
          cvSaveImageBlob(filename.str().c_str(), img, it->second);
          blobNumber++;

          std::cout << filename.str() << " saved!" << std::endl;
        }*/
        break;
    }
    cvReleaseBlobs(blobs);

}

    //frameNumber++;
  //}}}

  cvReleaseStructuringElement(&morphKernel);
  cvReleaseImage(&frame);
  cvReleaseImage(&framel);

  cvDestroyWindow("red_object_tracking=blue");
  cvDestroyWindow("red_object_tracking=red");
  return 0;
}
