# https://pluscoloring.com/search-Disney.htm
# https://pluscoloring.com/search-Sonic-hedgehog.htm
def sketch_image(photo, k_size, scale ):
    #Read Image
    img=cv2.imread(photo)
    
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img

    # Blur image
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)

    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img

    # Sketch Image
    sketch_img=cv2.divide(grey_img,invblur_img, scale=scale)

    # Save Sketch 
    cv2.imwrite('sketch.jpg', sketch_img)

    # Display sketch
    #cv2_imshow(sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
