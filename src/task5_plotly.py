import numpy as np
import pandas as pd
import plotly.express as px

def create_interactive_plotly(df):
    fig = px.scatter(df, x='x', y='y', title='Interactive Scatter Plot', 
                     labels={'x': 'X-Axis', 'y': 'Y-Axis'}, 
                     hover_data=['x', 'y']) 
    
    fig.show()
    return fig

df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
create_interactive_plotly(df)
