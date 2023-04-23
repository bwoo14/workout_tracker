import io
import base64
import numpy as np
import matplotlib.pyplot as plt

def create_line_plot(x, y, name = 'Measurement'):
    # Create figure and axis
    fig, ax = plt.subplots()

    # Plot the line
    ax.plot(x, y)

    # Set y-axis limits based on the data range
    ax.set_ylim(min(y), max(y))

    # Set the x-axis tick label size
    ax.tick_params(axis='x', labelsize=7)

    ax.set_title(name)
    ax.set_xlabel('Date')

    if name == 'Weight':
        ax.set_ylabel('Weight (lbs)')
    elif name == 'Body Fat':
        ax.set_ylabel('Body Fat (%)')
    elif name == 'Bicep Measurement':
        ax.set_ylabel('Bicep Measurement (inches)')
    elif name == 'Chest Measurement':
        ax.set_ylabel('Chest Measurement (inches)')
    elif name == 'Waist Measurement':
        ax.set_ylabel('Waist Measurement (inches)')


    # Save the plot as a PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image = buffer.getvalue()
    buffer.close()
    image_encoded = base64.b64encode(image).decode('utf-8')

    return image_encoded
