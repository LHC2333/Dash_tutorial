'''to get dash, you need to do pip/conda install
dash dash-renderer dash-html-components dash-core-components
plotly'''
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children = [
    html.H1('Dash Tutorial'),
    dcc.Graph(id='example',
              figure={
                'data': [
                    {'x':[1,2,3,4,5],'y':[6,7,8,9,10],'type':'line','name':'boat'},
                    {'x':[1,2,3,4,5],'y':[6,5,7,3,8],'type':'bar','name':'car'}
                ],
                 'layout':{
                    'title':'Basic Dash Example'
                 }
              })
])

if __name__ == '__main__':
    app.run_server(debug=True)
