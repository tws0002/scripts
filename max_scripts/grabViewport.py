import MaxPlus
class BitmapTypes(object):
    BMM_NO_TYPE  = 0  # Not allocated yet
    BMM_LINE_ART = 1  # 1-bit monochrome image
    BMM_PALETTED = 2  # 8-bit paletted image. Each pixel value is an index into the color table.
    BMM_GRAY_8   = 3  # 8-bit grayscale bitmap.
    BMM_GRAY_16  = 4  # 16-bit grayscale bitmap.
    BMM_TRUE_16  = 5  # 16-bit true color image.
    BMM_TRUE_32  = 6  # 32-bit color: 8 bits each for Red, Green, Blue, and Alpha.
    BMM_TRUE_64  = 7  # 64-bit color: 16 bits each for Red, Green, Blue, and Alpha.
    BMM_TRUE_24  = 8  # 24-bit color: 8 bits each for Red, Green, and Blue. Cannot be written to.
    BMM_TRUE_48  = 9  # 48-bit color: 16 bits each for Red, Green, and Blue. Cannot be written to.
    BMM_YUV_422  = 10 # This is the YUV format - CCIR 601. Cannot be written to.
    BMM_BMP_4    = 11 # Windows BMP 16-bit color bitmap.  Cannot be written to.
    BMM_PAD_24   = 12 # Padded 24-bit (in a 32 bit register).  Cannot be written to.
    BMM_LOGLUV_32 = 13
    BMM_LOGLUV_24 = 14
    BMM_LOGLUV_24A    = 15
    BMM_REALPIX_32    = 16 # The 'Real Pixel' format.
    BMM_FLOAT_RGBA_32 = 17 # 32-bit floating-point per component (non-compressed), RGB with or without alpha
    BMM_FLOAT_GRAY_32 = 18 # 32-bit floating-point (non-compressed), monochrome/grayscale
    BMM_FLOAT_RGB_32 = 19
    BMM_FLOAT_A_32 = 20

def ActiveViewport(filename=(MaxPlus.PathManager.GetRenderOutputDir() + r'default.tif')):
    ext = '.tif'
    storage = MaxPlus.Factory.CreateStorage(6)
    bmi = storage.GetBitmapInfo()
    grab = MaxPlus.Factory.CreateBitmap()

    vm = MaxPlus.ViewportManager
    av = vm.GetActiveViewport()
    av.GetDIB(bmi, grab)
    
    bmi.SetWidth(400)
    bmi.SetHeight(400)            
    bmi.SetName(filename + ext)

    bmp = MaxPlus.Factory.CreateBitmap(bmi)
    bmp.CopyImage(grab, 2, 1)
    grab.Close(bmi)

    bmp.OpenOutput(bmi)
    bmp.Write(bmi)
    bmp.Close(bmi)
    print 'asdf'

    return bmp

ActiveViewport()        