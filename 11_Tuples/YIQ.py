def yiq(rgb):
    yiq_1 = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    yiq_2 = 0.596 * rgb[0] - 0.274 * rgb[1] - 0.322 * rgb[2]
    yiq_3 = 0.211 * rgb[0] - 0.523 * rgb[1] + 0.312 * rgb[2]

    yiq_code = (round(yiq_1, 4), round(yiq_2, 4) , round(yiq_3, 4))

    return yiq_code
