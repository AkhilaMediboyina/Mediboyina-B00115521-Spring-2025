import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def plot_bar_chart(df, column):
    """Generate a bar chart for a selected column."""
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=column, palette="viridis")
    plt.title(f"Distribution of {column}")
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    encoded = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return encoded
