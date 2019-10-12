#! /usr/bin/env python
#
#   File = example-jpeg-to-xcf.py
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################
#
from gimpfu import *
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

from funcs import *

#import re
#
def DC_edit(srcFile):
    """Registered function exampleJpgToXcf, Converts all of the
    jpegs in the source directory into xcf files in a target 
    directory.  Requires two arguments, the paths to the source and
    target directories.  DOES NOT require an image to be open.
    """
    ###
    
    dirname, filename1, filename2 = editpdftopng(srcFile)
    
    item, quanti, desti = findRE(filename1)
    
    image = pdb.file_png_load(filename1, filename1)
#    image = pdb.file_pdf_load(dirname+'/'+fname1,dirname+'/'+fname1)
#    pdb.gimp_image_set_resolution(image, 3508, 2480)
    
    drawable = image.active_drawable
    
    pdb.gimp_message(image)
    
    pdb.gimp_message(pdb.gimp_image_get_layers(image))
    
    pdb.gimp_message('image layers')
    pdb.gimp_message(image.layers)
    
    operation = 2 # cut
    x = 250
    y = 108
    width = 1288
    height = 424    
    pdb.gimp_image_select_rectangle(image, operation, x, y, width, height)
    selection = pdb.gimp_image_get_selection(image)
#    pdb.gimp_layer_remove_mask(image.layers[0], 0)
#    active_channel = pdb.gimp_image_get_active_channel(image)
    pdb.gimp_message(selection)
    
    pdb.gimp_context_set_default_colors()
    pdb.gimp_context_swap_colors()
    
    pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 255, 0, 1, 0, 0, 0)
    
    operation = 2 # cut
    x = 250
    y = 2198
    width = 1288
    height = 148
    pdb.gimp_image_select_rectangle(image, operation, x, y, width, height)
    
    pdb.gimp_edit_bucket_fill_full(drawable, 0, 0, 100, 255, 0, 1, 0, 0, 0)
    pdb.gimp_selection_none(image)
    
    raw_filename = filename1
    vectorize = 0
    ignore_hidden = 0
    apply_masks = 0
    interlace = 0
    compression = 0
    
    pdb.file_png_save(image, drawable, filename1, raw_filename, interlace, compression, 1, 1, 1, 1, 1)
    
    image2 = pdb.file_png_load(filename2, filename2)
#    image2 = pdb.file_pdf_load(dirname+'/'+fname2,dirname+'/'+fname2)
#    pdb.gimp_image_set_resolution(image2, 2550, 3300)
    drawable2 = image2.active_drawable
    pdb.gimp_message(image2)
    
#    pdb.gimp_message(layer)
    
    
    operation = 2 # cut
    x = 33
    y = 2949
    width = 2421
    height = 261  
    pdb.gimp_image_select_rectangle(image2, operation, x, y, width, height)
    pdb.gimp_edit_bucket_fill_full(drawable2, 0, 0, 100, 255, 0, 1, 0, 0, 0)
    
    pdb.gimp_selection_none(image2)
    
    pdb.plug_in_autocrop(image2, drawable2)
#    pdb.plug_in_autocrop_layer(image, drawable)
#    pdb.gimp_image_scale(image2, 374, 491)
        
#    filename2 = filename2
    raw_filename = filename2
    vectorize = 0
    ignore_hidden = 0
    apply_masks = 0
    interlace = 0
    compression = 0
    
    pdb.file_png_save(image2, drawable2, filename2, raw_filename, interlace, compression, 1, 1, 1, 1, 1)
    
    pdb.gimp_selection_all(image2)
    
    non_empty = pdb.gimp_edit_copy(drawable2)
    
    floating_sel = pdb.gimp_edit_paste(drawable, 0)
    
    pdb.gimp_layer_scale(floating_sel, 1000, 1206, 0)
    
    pdb.gimp_layer_translate(floating_sel, 1950, 670)
    
#    pdb.gimp_layer_resize(floating_sel, 1000, 1206, 1640, 752)
    
#    pdb.gimp_floating_sel_anchor(floating_sel)
    
#    pdb.file_pdf_save(image2, drawable2, filename2, raw_filename, vectorize, ignore_hidden, apply_masks)
#    pdb.gimp_layer_scale(layer, 374, 491, 0)
#    pdb.gimp_layer_translate(layer, 800, -250)
#    layer = pdb.gimp_image_merge_down(image, layer, 2)
    
#    pdb.gimp_image_delete(selection)
#    pdb.gimp_image_remove_layer(image, image.layers[1])
#    pdb.gimp_edit_clear(selection)
#    pdb.gimp_item_delete(selection)
    
#    os.path.splitext(os.path.basename(srcFile))
    
    filename = dirname+'/'+'DC'+quanti+'x'+item+'-'+desti+'.pdf'
    raw_filename = filename
    vectorize = 0
    ignore_hidden = 0
    apply_masks = 0
    
    pdb.file_pdf_save(image, drawable, filename, raw_filename, vectorize, ignore_hidden, apply_masks)
    
#    for img in pdb.gimp_image_list()[1] :
#        pdb.gimp_image_delete(img)
    
#
############################################################################
#
register (
    "DC_edit",         # Name registered in Procedure Browser
    "Edit DC to print", # Widget title
    "Edit DC to print", # 
    "Julio Pimentel",         # Author
    "Julio Pimentel",         # Copyright Holder
    "October 2019",            # Date
    "DC Edit", # Menu Entry
    "",     # Image Type - No image required
    [
    ( PF_FILENAME, "srcFile", "JPG Originals (source) Directory:", "" ),
#    ( PF_FILENAME, "tgtFile", "XCF Working (target) Directory:", "" ),
    ],
    [],
    DC_edit,   # Matches to name of function being defined
    menu = "<Image>/DC_edit"  # Menu Location
    )   # End register

main()
