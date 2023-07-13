from recipe_app.models import Recipe_app, Recipe_ingredient
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_recipename_from_id(val):
    #get the recipe name from the id
    recipename = Recipe_app.objects.get(id=val)
    return recipename

def get_graph():
   #create a BytesIO buffer for the image
   buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retrieve the content of the file
   image_png=buffer.getvalue()

   #encode the bytes-like object
   graph=base64.b64encode(image_png)

   #decode to get the string as output
   graph=graph.decode('utf-8')

   #free up the memory of buffer
   buffer.close()

   #return the image/graph
   return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')

    fig = plt.figure(figsize=(6, 3))

    if chart_type == '#1':
        plt.bar(data['name'], data['minutes'])

    elif chart_type == '#2':
        labels = kwargs.get('labels')
        plt.pie(data['minutes'], labels=labels)

    elif chart_type == '#3':
        plt.plot(data['name'], data['minutes'])
    else:
        print('unknown chart type')

    plt.tight_layout()

    chart = get_graph()
    return chart