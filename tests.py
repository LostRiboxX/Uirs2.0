from crop import croped
from filter import filter
from diff import imgContours
from cont import drawconts
from tests1 import drawconnectionslines

imgnameprime = '1.jpg'

dict = {'red': 10,'blue' : 4, 'gray' : 1, 'darkgray' : 5, 'lightgreen' : 2, 'green' : 3, 'pink' : 2, 'lightbrown' : 4, 'brown' : 5}
seq1 = ['gray', 'blue' , 'brown', 'lightgreen','lightgreen', 'red', ' gray', 'brown', 'red8', 'darkgray', 'gray', 'lightgreen', 'brown', 'red', 'green', 'darkgray', 'gray16', 'blue', 'gray', 'pink', 'lightgreen', 'green', 'lightbrown']
seq2 = ['gray','lightgreen','green','lightbrown','pink','darkgray','blue','gray','green','gray','red','lightbrown','red','darkgray','brown','blue','lightgreen','brown','gray18','red','gray','lightgreen','gray','blue', 'lightgreen']
seq3 = ['red','lightbrown','gray','blue','brown', 'lightgreen', 'darkgray','green','gray8','darkgray', 'brown','red', 'pink', 'red', 'lightgreen', 'blue', 'brown16','blue','gray','gray','green','lightgreen','brown','lightgreen','gray','gray']
imgcroped = croped(imgnameprime)

imgfiltered = filter(imgcroped)

imgconts = imgContours(imgfiltered)

centersmass, contours = drawconts(imgconts,imgcroped)

connections = drawconnectionslines(imgcroped, contours, centersmass, 100)

