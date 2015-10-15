def findFeaturePositions(imgarray):
    #imgarray = edges[1]
    im = cv2.cvtColor(imgarray, cv2.COLOR_GRAY2RGB)
    im_rotate = np.swapaxes(im,0,1)
    
    # build an array where we add up the intensity of the y-axis
    # normalize to percentage
    # reduce to single digit
    # reduce to terniary 0,1,2 where 0 is empty, 1 are features, 2 are creases
    
    x_axis = []
    x_axis_values = []
    for x in im_rotate:
        rsum = 0
        for y in x:
            rsum += y[1]
        x_axis_values.append(((rsum/255)*100)/height)
        num = ((rsum/255)*100)/height
        num = int(round(num, -1))
        num = num/10
        #x_axis.append(num)
        if num > 0 and num <= 4:
            num = 1
        elif num >= 5: # 9 would be straight line, need to account for slightly skewed lines
            num = 2
        x_axis.append(num)
    return x_axis_values
    
    
    plt.plot(x_axis_values)
    # go through x_axis and find chunks of 0, 1-5, 6-10
    i = 0
    blocks = []
    blocks.append(0)
    while i < len(x_axis):
        while x_axis[i] == x_axis[i + 1]:
            i = i + 1
            if i + 1 == len(x_axis):
                break
        i = i + 1
        blocks.append(i)
    
    i = 0
    empty_blocks = []
    empty_blocks.append(0)
    while i < len(x_axis_values):
        while x_axis_values[i] == x_axis_values[i + 1]:
            i = i + 1
        i = i + 1
        empty_blocks.append(i)
    blocks = empty_blocks

       
    block_length = []
    for x in range(0, len(blocks)):
        if x + 1 == len(blocks):
            pass
        else:
            block_length.append(blocks[x+1] - blocks[x])
    
    big_blocks = [i for i, x in enumerate(block_length) if x > (width * 0.02)]

    # cover should be the busiest and longest block
    cover_block = max(block_length)
    
    margin = int(width * 0.01)
    f = 0
    for x in range(0, block_length.index(cover_block)):
        f = f + block_length[x]
    cover_fi_pos = f - margin
    f + cover_block

    # go through the blocks and find their positions
    interesting = []
    for x in big_blocks:
        f = 1
        for y in range(0, x + 1):
            f = f + block_length[y]
        interesting.append(f)
    
    # find creases
    creases = [i for i, x in enumerate(x_axis) if x == 2]
    return interesting

feature_pos = findFeaturePositions(edges[2])
