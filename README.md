
# Dataset

- resized original images <br>
(d1)512 X 512 https://www.kaggle.com/xhlulu/panda-resized-train-data-512x512 <br>

- tiled images <br>
(d2) (one img)level 1, 128X128X16(resize to 512X512) https://www.kaggle.com/muerbingsha/pandatiled <br>
(d3) (tiles)level 1, 128X128X16(resize to 512X512) https://www.kaggle.com/muerbingsha/pandatiledsingle <br> 
(d4) level 2, 256X256X36 (resize to 512X512) based on original competition data (for kaggle kernels) <br>
(d5) level 2, 256X256X36 <br>
(d6) level 2, 256X256X36 (resize to 512X512) based on the cropped version https://www.kaggle.com/lopuhin/panda-2020-level-1-2 since colab cannot host original competition data (for colab kernels) <br>
(d7) dynanic tiling 

- remove pen marks

# Models
EfficienetNet-B0 <br>
EfficienetNet-B4 <br>
serenet50 <br>

# Loss
CrossEntropyLoss <br>
MSELoss <br>
Softmax + CrossEntropyLoss <br>
BCELossWithLogits <br>



# Experiments 
### Classification
| Dataset | image size| Model | loss | LB | Info | 
|:--:|:--:|:--:|:--:|:--:|:--:|
|d1|512X512 | EfficientNet-B4| Softmax + CrossEntropyLoss | 0.59| 4 epochs + all data |
|d1|512X512 | EfficientNet-B4| Softmax + CrossEntropyLoss | 0.62 | 10 epochs + all data + ReduceLROnPlateau(cohen)|
|d1|512X512 | EfficientNet-B4| Softmax + CrossEntropyLoss | 0.62 | 10 epochs + all data + ReduceLROnPlateau(loss)|
|d2|512X512 | EfficientNet-B4| Softmax + CrossEntropyLoss | 0.64 | 4 epochs + all data |
|d2|512X512 | EfficientNet-B4| Softmax + CrossEntropyLoss | 0.70 | 20 epochs + all data + ReduceLROnPlateau(loss) |
|d2|512X512 | EfficientNet-B4| Softmax + CrossEntropyLoss | 0.71 | 30 epochs + all data + ReduceLROnPlateau(loss) |
|d1|512X512 | seresnet50 | Softmax + CrossEntropyLoss | 0.2 |1 epoch + all data|
|d1|512X512 | seresnet50 | Softmax + CrossEntropyLoss | 0.49 |10 epochs + 1000 samples|
|d1|512X512 | seresnet50 | Softmax + CrossEntropyLoss | 0.58 |10 epochs + 2000 samples|
|d1|512X512 | seresnet50 | Softmax + CrossEntropyLoss | 0.61 |20 epochs + 2000 samples + ReduceLROnPlateau(cohen)|
|d1|512X512 | seresnet50 | Softmax + CrossEntropyLoss | 0.65 |20 epochs + all samples + ReduceLROnPlateau|
|d2|512X512 | seresnet50 | Softmax + CrossEntropyLoss | 0.70 |20 epochs + all samples + ReduceLROnPlateau|
|d3|512X512 | seresnet50 | Softmax + CrossEntropyLoss | ? | 1 epochs + all samples + ReduceLROnPlateau + each tile augmentation + 8folds|

### Regression
| Dataset | image size| Model | loss | LB | Info | 
|:--:|:--:|:--:|:--:|:--:|:--:|
|d3|512X512 | seresnet50 | MSELoss | 0.71 | 10 epochs + 1000 samples + each tile augmentation |
|d3|512X512 | seresnet50 | MSELoss | 0.77 | 10 epochs + all samples + each tile augmentation |
|d3|512X512 | seresnet50 | MSELoss | 0.78 | 20 epochs + all samples + each tile augmentation |
|d3|512X512 | seresnet50 | MSELoss | 0.77 | 10 epochs + 1000 samples + each tile augmentation + 2 color augs(final) |
|d3|512X512 | seresnet50 | MSELoss | 0.76 | 10 epochs + 1000 samples + each tile augmentation + 2 color augs(best) |
|d3|512X512 | seresnet50 | MSELoss | 0.78 | 10 epochs + all samples + each tile augmentation + 2 color augs(best) |
|d4|512X512 | seresnet50 | MSELoss | ? |  |
|d5|1536X1536 | seresnet50 | MSELoss | ? |  |
|d3|512X512 | EfficientNet-B4 | MSELoss | ? |  |
|d4|512X512 | EfficientNet-B4 | MSELoss | ? |  |
|d5|1536X1536 | EfficientNet-B4 | MSELoss | - | impossible, 1536 only suitable in Efn-B0  |

| Dataset | image size| Model | loss | LB | Info | 
|:--:|:--:|:--:|:--:|:--:|:--:|
|d4| 512X512 | EfficientNet-B4 | MSELoss | 0.76 | local predict cohen is 0.7732, about 5 epochs |
|d4| 512X512 | EfficientNet-B4 | MSELoss | 0.76 | local predict cohen is 0.7865, about 5 epochs, mode0 + model2 |
|d4| 512X512 | EfficientNet-B4 | MSELoss | 0.73 | more epochs 3+ I guess train_test_split is still problematic, change to 8 fold |
|d7| 512X512 | EfficientNet-B4 | MSELoss | 0.74 | fold 0, many epochs |
|d7| 768X768 | EfficientNet-B4 | MSELoss | ? | fold 0, 3 epochs |
|d4| 512X512 | EfficientNet-B4 | MSELoss | ? | 8 fold, 3 epochs |
|d6| 512X512 | seresnetxt-50 | MSELoss | ? | 8 fold, 3 epochs |
|d5| 1536X1536 | EfficientNet-B0 | BCELossWithLogits | 0.69 | local val cohen is 0.74, 2 epochs|
|d7| 1536X1536 | EfficientNet-B0 | BCELossWithLogits | 0.81 | fold 0, trained based on provided checkpoint | 


### Ensemble



# Conclusion
- more data, more epochs(at least 20) works!!
- not much difference between efn-b4 and serenset50
- d2 is better than d1
- regression is better than classification
- data is not covered for the above last experiment
- best model doens't necessary bettert than final. Should use the version having the highest val(1, test_dl) score



# Model size comparison
|Model | Size(MB) |
|:--:|:--:|
|Efficienet-B4|2832.72|
|Efficienet-B5|3903.49|
|Efficienet-B6|5010.21|
|Efficienet-B7|6736.80|
|seresnet50|2406.75|
|seresnet200b|7698.62|


# Works to do 
### 2020/5/30/
1) investigate coef not updated <br>
2) test color (brightness, saturation, hue variance) augumentation <br>
3) test 8 folds <br>
4) test efn-b4 model



