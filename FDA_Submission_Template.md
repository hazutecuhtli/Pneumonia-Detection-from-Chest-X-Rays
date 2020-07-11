# FDA  Submission

**Your Name:**

Alfonso Sanchez

**Name of your Device:**

Pneumy

## Algorithm Description 

### 1. General Information

**Intended Use Statement:** 

The device is intended to be used to determine if a patient is affected by pnuemonia. The device should be used always a complement, they findinds needs to be corroborated by an specialist to determine how probable is for they users to be affected by pnemonia.

**Indications for Use:**

It was designed to be used on x_ray images of the lower respiratory system. This, to determine if patients suffer from pneumonia conditions or not. To be more specific, because of the device properties, to determine how probable is for a patient to be affected by pneumonia accordingly to the following properties:
 
The device was tuned to be more sensitive to positive pneumonia cases, since its precision score value is high for positive cases of pneumonia, while its recall score value is low for the same case. Therefore, when the device determine that a patient is not affected by pneumonia, it has higher probability for that be the case, compared when the device detects that a patient is affected by the same condition.  

A higher precision value is obtained when the amount of true positive cases detected by the device is bigger than the sum of cases that were correctly and incorrectly detected as positive cases. On the other hand, a low recall value is the result of the amount of positive detected cases which is small compared with the sum of correctly detected positive cases with the amount of incorrectly detected negative cases.

**Device Limitations:**

The device should not be used for persons older than 80 and as a concluding diagnostic. 

**Clinical Impact of Performance:**

It was designed to be used in patients wiht ages in the rage of 1 to 80 years old.

Additionally, the system was designed to be used in patients affected by the following deaseses:

- Infiltration
- Effusion
- Atelectasis

### 2. Algorithm Design and Function

<< Insert Algorithm Flowchart >>

**DICOM Checking Steps:**

DICOM files are used to get information about patients, especially their names and images associated with them, including the characteristics of those images, which should match the expected to be valid for their use. Among the images, characteristics to be considered as valid include the part of the body related to the image, how was acquired and the type of image. 

**Preprocessing Steps:**

The preprocessing of the data proviced is achieved by determinen diseases associated with the patients of interest, as well as finding their images associated. The lasts are normalized and augmentes to increase the performance of thge method used to classify images. 

Normalizations are implemented by scaling their pixel amplitudes to 1 and to substract the averaged mean accross all validation images. Additionally, their variance are reduced by dividing the images pixels by the averaged standar deviateion. 

Augmentation was implemented by rotating, randomly, their images in a range of 45 degrees. The images were also flip, shift and zoom to some degree.

**CNN Architecture:**

![Alt text](Images/CNN_Arch.png?raw=true "CNN Architecture")

### 3. Algorithm Training

**Parameters:**
* Types of augmentation used during training

- horizontal_flip = True 

- vertical_flip = False

- height_shift_range= .1 

- width_shift_range= .1

- rotation_range= 15

- shear_range = .1

- zoom_range=.1

* Batch size

- validation_batch = 1000
  
- training_batch = 100
  
- network_batch = 50

* Optimizer learning rate

- Adam = 1e-5

* Layers of pre-existing architecture that were frozen

- VGG imagenet frozen layers = 18

* Layers of pre-existing architecture that were fine-tuned

- VGG imagenert re-trained layers = 1

* Layers added to pre-existing architecture

- Added layers to the VGG imagenet transfer learning = 8

<< Insert algorithm training performance visualization >> 

![Alt text](Images/TrainingPerf.png?raw=true "Training log")

<< Insert P-R curve >>

![Alt text](Images/Pre-Rec.png?raw=true "Precision - Recall curve")

**Final Threshold and Explanation:**

The threshold value selected for the use of the device is .64. This, as explained before, to obtain a high precision value and a low recall value for the device, to increase the sensitivity of the device, the number of positive cases detected compared with the sum of correctly positive cases detected with the sum of incorrectly detected negative cases.  

### 4. Databases
 (For the below, include visualizations as they are useful and relevant)

**Description of Training Dataset:** 

The training dataset was composed of images provided for the analysis. In addition, images were augmented to increase the algorithm generalisation of cases related to the disease of interest, as shown below.

![Alt text](Images/Training.png?raw=true "Training Images")

The training dataset was generated from the provided set of images and patients information related to different lower respiratory system-related diseases. It was generated by dividing the data into two different datasets, the training and validation datasets. However, there were fewer cases related to pneumonia in comparison to cases not affected. Then, the dataset used to get the training and validation datasets were reduced, selecting the same number of cases not affected by pneumonia than cases affected by pneumonia.

The balance of classes of interest was implemented to reduce imbalances which can be translated into a bias towards a specific class, decreasing the performance of the device implemented. Thus, the training dataset was generated selecting, randomly, 70% of the remaining cases in the provided dataset. 

Additionally, the images used for the training of the model that compose the presented device were increased by augmenting them, as explaining at the beginning of this section. 

**Description of Validation Dataset:** 

As in the previous case, images used for the validation dataset were obtained from the provided data for the analysis. The difference is that these were not augmented:

![Alt text](Images/Validation.png?raw=true "Validation Images")

The remaining 30% of the balanced provided dataset of images and patient characteristics were used to generate the validation dataset. In comparison with the training dataset, images that compose the validation dataset were not augmented, only normalized. The normalizations were applied to both datasets, to the training and validation dataset, as explained before in this document. 

### 5. Ground Truth

The ground truth was generated using a provided label for all patients diseases, related to the disease of interest, pneumonia.

### 6. FDA Validation Plan

**Patient Population Description for FDA Validation Dataset:**

The ideal dataset required to run the trained model should contain x_ray images related with their lower respiratory systems, they gender, age and if they are affected by diseases such as - Infiltration, Effusion and Atelectasis.

**Ground Truth Acquisition Methodology:**

The ground truth can be acquired from a specialist, to determine which of the patient's characteristics and x rays images can be related to pneumonia.

**Algorithm Performance Standard:**

The performance of the algorithm can be observed using the ROC curve and the F1 score curve obtained, presented in the following figures, respectively:

![Alt text](Images/ROCcurve.png?raw=true "ROC curve")

![Alt text](Images/F1score.png?raw=true "F1 score")

The ROC curve shows that the device is able to classify the images of interest as positive and negative cases of pneumonia. This, since the obtained curve, shown in red, is not lineal as the show blue line, meaning that the classification is not based on random selection. The AUC of the ROC curve also let us know that the device is also able to perform the desired classification of images. Unfortunately, the obtained values are not higher enough to rely on the device alone for a correct diagnostic.

Furthermore, the F1 score curve presented in the previous figures shown that the algorithm, for the selected threshold of .64, is more sensitive towards the detection of positive cases, corrected or incorrectly detected cases. Then, the performance of the presented device relies on that, on detecting correctly negative cases of pneumonia. For the selected threshold value, an F1 score value of .42 was obtained. 

The results obtained can be compared against well-established literature related to the use of AI for the classification of similar diseases, as the *CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning* study presented by *Pranav Rajpurkar* among others. When comparing the results obtained at its the mentioned article results, it can be seen that the AUC for the ROC curve obtained is smaller than the results presented in the article, as well as the F1 score. The difference is greater than .1 for the ROC curve and about .3 for the F1 score value obtained. However, this comparison is not accurate, since we do not have the same dataset used for testing the CheXNet. 

Nonetheless, the presented device is shown, with the explained device performance, that it is able to help specialist discarding pneumonia cases from patients using X_ray images. 