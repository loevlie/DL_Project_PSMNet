# Introduction to Deep Learning Project Repo.
## PSMNet Replication and Modification 

A PSMNet model was developed based on the literature [[1]](#1).  This was used to generate disparity maps and they were tested based on the training L1 loss and validation 3-pixel accuracy.  The baseline PSMNet architecture from [[1]](#1) is shown in Figure (1).  

![PSMNet Baseline  Architecture](./Images/Architecture_PSMNet.png)

Three main modification to the architecture of the model were also tested. 

1. Less Convolutional layers
2. More Convolutional layers
3. Asymmetric Convolutions when the kernal size was large. 

These modifications to the baseline PSMNet model all reached the same minima (at differing amounts of Epochs).  Figures for the changes in loss and accuracy are shown below.  

![L1 Loss Experiments](./Images/L1_loss.png)
![3-pixel Accuracy Experiments](./Images/Accuracy.png)

The asymmetric convolutions idea was based on the paper "Rethinking the Inception Architecture for Computer Vision" [[2]](#2).  It has been shown in the literature that the asymmetric convolutions are equivilant to sliding a two layer network with the same receptive field as in a 3x3 convolution.  This is illustrated in figure 3.  The change to the basic block in the PSMNet architecture is shown in figure 4.  

![Mini-network replacing the 3x3 convolutions [[2]](#2)](./Images/Spatial_Factorization.png)
![Comparison between the original and the modified architecture with asymmetric convolutions](./Images/Parameter_Reduction.png)

## References
<a id="1">[1]</a> 
Jia{-}Ren Chang and Yong{-}Sheng Chen (2018). 
Pyramid Stereo Matching Network
CoRR, abs/1803.08669, http://arxiv.org/abs/1803.08669

<a id="2">[2]</a> 
Christian Szegedy and
               Vincent Vanhoucke and
               Sergey Ioffe and
               Jonathon Shlens and
               Zbigniew Wojna (2015). 
Rethinking the Inception Architecture for Computer Vision 
CoRR, abs/1512.00567, http://arxiv.org/abs/1512.00567

