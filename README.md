# Centroids as Internal Representations of Image Data

As you imagine concepts and objects inside of your head, you might have noticed that you have internal "representations" of various objects and concepts. Ever wonder what a computer thinks the numbers 0-9 look like?

<div align="center">
    <img src="./assets/mnist.png" alt="plts"/>
</div>

Pretty cool huh? It also turns out that its quite simple to really peek inside of statistical models! In this work we find that with sufficient MNIST image data, simple cluster algorithms (like k-means) centroid's are visually identifiable representations of the classes present in image datasets.

<img src="./assets/fmnist2.png" alt="plts"/>

In order to further test out our method, we tried used [Fashion-MNIST](https://en.wikipedia.org/wiki/Fashion_MNIST). Notice how there are clearly identifiable and unique reprentations for boots, sneakers, and shoes. These initial findings show that clustering algorithms can hold visual concepts inside of their centroids, and suggest further research into unsupervised methods for data representations.

## Paper
The complete project write up is compiled in a PDF format as well as a Google Doc. You can access either of these by clicking the link below:

[Write-up PDF](./assets/4022%20Project%20Write-up.pdf) | [Write-up Link](https://docs.google.com/document/d/1jfs_Y3a3PV33UePfLRl7O0zu-oGrzLDcF12To9LohM0/edit?usp=sharing). 

Don't want to read long papers? Check out a summarized version from our [presentation](https://docs.google.com/presentation/d/1LgfTgp0mLIOAv0NgphH1Dabi6m-mlunv26zONNy2kFc/edit?usp=sharing).


## Code
Interested in the code? We have a jupyter notebook with our findings at ```research/main.ipynb```. 

If you want to experiment with the notebook, make sure to run the following commands.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```