import openslide
wsi = openslide.OpenSlide("/project/hnguyen2/mvu9/datasets/TGCA-datasets/KICH/bb078404-fd12-4f27-9d23-0fc412e76a52/TCGA-UW-A7GX-11Z-00-DX1.57C4FD28-5463-40C5-9E87-484F3326B395.svs")
print(wsi.level_dimensions)