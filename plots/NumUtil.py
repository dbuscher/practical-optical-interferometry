import numpy as np

def Sum2d(a):
    """"Sum over the rightmost two dimensions of an array of dimension >= 2"""
    return(np.sum(np.sum(a,-1),-1))

def ModSquared(x): return( (np.abs(x)**2 ))

def RadiusSquared(ny, nx, style=None,centre=None):
    '''Generate a 2d array with values equal to the square of the radius from
    a given centre coordinate. If style="FFT" then the pixel coordinate system
    wraps around so that pixels at coordinates > nx/2 or >ny/2 represent
    negative coordinates. The centre coordinate is either (0, 0) pixel (style
    = "FFT") or at a user-defined location, defaulting to the centre of the
    array. Note that the centre coordinate cannot be changed for style="FFT".
    '''
    if (style == 'FFT'):
        x = np.arange(nx)
        x[nx/2:] = nx - x[nx/2:]
        y = np.arange(ny)
        y[ny/2:] = ny - y[ny/2:]
    else:
        if centre is None:
            centre=((nx-1.0)/2.0,(ny-1.0)/2.0)
        x = np.arange(nx) - centre[0]
        y = np.arange(ny) - centre[1]
    return np.add.outer(y**2, x**2)

def CircularMask(radius, ny, nx, style='centred'):
    return np.less_equal(RadiusSquared(ny, nx, style), radius**2)

def Radius(ny, nx, style='centred',centre=None):
    return np.sqrt(RadiusSquared(ny, nx, style,centre))

def Smiley(nx, ny):
    '''Generate a checkerboard pattern of 1s and -1s for pre-correcting FFTs'''
    xSmiley = np.bitwise_and(np.arange(nx),1)*2 - 1.0
    ySmiley = np.bitwise_and(np.arange(nx),1)*2 - 1.0
    return np.multiply.outer(xSmiley, ySmiley)

def test():
    print(Radius(3, 4))

if __name__ == '__main__': test()
