import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from PIL import Image

def PlotDiseasesAge(df, Feat,pneumonia=None, Labels=True):
    
    if pneumonia == True:
        df = df[df.pneumonia == 1]
    elif pneumonia == False:
        df = df[df.pneumonia == 0]
        
    df_groups = df.groupby(Feat)
        
    GroupLabels = []
    for disease in df.columns[-14:]:
        Disease = []
        for group in df_groups.groups.keys():
            Disease.append(df_groups.get_group(group)[disease].sum())
        GroupLabels.append(Disease) 
            
    cmap = plt.get_cmap('hsv')
    lines = ['-', '--', '-.']*5
    colors = [cmap(i) for i in np.linspace(0, 1, 14)]

    plt.figure(figsize=(12,7))
    for n in range(len(GroupLabels)):
        plt.plot(GroupLabels[n], color=colors[n], linestyle=lines[n],label=df.columns[-14:][n]);  
    if Labels == True:
        plt.legend(loc="upper left");
    plt.title('Diseases Vs Population Age')
    plt.xlabel('Population Age')
    plt.ylabel('Diseases Count')
    plt.grid(True)
    

def PlotDiseases(df, feature, pneumonia=None, pallete='hls'):
   
    Max_Len = 14

    if pneumonia == True:
        df = df[df[feature] == 1]
        df.drop(feature, axis=1, inplace=True)
        Max_Len = 13
    elif pneumonia == False:
        df = df[df[feature] == 0]
        df.drop(feature, axis=1, inplace=True)
        Max_Len = 13

    
    labels = df[df.columns[-Max_Len:]].sum().sort_values(ascending=False).index.tolist()
    bars = df[df.columns[-Max_Len:]].sum().sort_values(ascending=False).tolist()
    
    plt.figure(figsize=(10,5))
    sns.barplot(x=labels, y=bars,palette=pallete)
    plt.xticks(rotation=90)
    plt.title('Diseases')
    plt.ylabel('Diseases Occurrence')    
    plt.grid(True)
    
def ImagesAndSpectrum(df, num, pnue, size=(15,7), title='', threshold = None):
    
    img = Image.open(df[df.pneumonia == pnue].path.iloc[num])

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,5))
    plt.suptitle(title)
    
    if threshold == None:
        ax1.imshow(np.asarray(img),cmap='gray');
    else:
        ax1.imshow(np.multiply(np.asarray(img),(np.asarray(img) > threshold).astype(int)), cmap='gray')
    
    ax1.set_title('X-ray')

    if threshold == None:
        ax2.hist(list(img.getdata()), bins = 256);
    else:
        ax2.hist(np.asarray(img)[(np.asarray(img) > threshold)],bins=256);

    ax2.set_title('X-ray spectrum')
        
    plt.grid(True) 
    
def spectrums(all_xray_df):
    
    samples = 10

    df_11 = all_xray_df[all_xray_df.pneumonia == 1].path.sample(samples).tolist()
    df_12 = all_xray_df[all_xray_df.pneumonia == 1][all_xray_df.infiltration == 1].path.sample(samples).tolist()
    df_13 = all_xray_df[all_xray_df.pneumonia == 1][all_xray_df.atelectasis == 1].path.sample(samples).tolist()
    df_14 = all_xray_df[all_xray_df.pneumonia == 1][all_xray_df.effusion == 1].path.sample(samples).tolist()    
    df_01 = all_xray_df[all_xray_df.pneumonia == 0].path.sample(samples).tolist()
    df_02 = all_xray_df[all_xray_df.pneumonia == 0][all_xray_df.infiltration == 1].path.sample(samples).tolist()
    df_03 = all_xray_df[all_xray_df.pneumonia == 0][all_xray_df.atelectasis == 1].path.sample(samples).tolist()
    df_04 = all_xray_df[all_xray_df.pneumonia == 0][all_xray_df.effusion == 1].path.sample(samples).tolist()

    Pnemy1 = []
    Pnemy0 = []

    n = 0
    for path_11, path_12, path_13, path_14 in zip(df_11, df_12, df_13, df_14):
        if n == 0:
            Pnemy1.append(list(Image.open(path_11).getdata()))
            Pnemy1.append(list(Image.open(path_12).getdata()))
            Pnemy1.append(list(Image.open(path_13).getdata()))
            Pnemy1.append(list(Image.open(path_14).getdata()))
            n = 1
        else:
            Pnemy1[0] += list(Image.open(path_11).getdata())
            Pnemy1[1] += list(Image.open(path_12).getdata())
            Pnemy1[2] += list(Image.open(path_13).getdata())
            Pnemy1[3] += list(Image.open(path_14).getdata())

    n = 0
    for path_01, path_02, path_03, path_04 in zip(df_01, df_02, df_03, df_04):
        if n == 0:
            Pnemy0.append(list(Image.open(path_01).getdata()))
            Pnemy0.append(list(Image.open(path_02).getdata()))
            Pnemy0.append(list(Image.open(path_03).getdata()))
            Pnemy0.append(list(Image.open(path_04).getdata()))
            n = 1
        else:
            Pnemy0[0] += list(Image.open(path_01).getdata())
            Pnemy0[1] += list(Image.open(path_02).getdata())
            Pnemy0[2] += list(Image.open(path_03).getdata())
            Pnemy0[3] += list(Image.open(path_04).getdata())   

    for n in range(4):
        Pnemy1[n] = [a/samples for a in Pnemy1[n]]
        Pnemy0[n] = [a/samples for a in Pnemy0[n]]      


    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=2, figsize=(15,18))

    plt.suptitle('Respiratory diseases spectrums')

    ax1[0].set_title('X-ray - Pneumonia (Average)')    
    ax1[0].hist([i for i in Pnemy1[0] if i >= 5],bins=256);
    ax1[0].grid(True)

    ax1[1].set_title('X-ray - No Pnuemonia (Average)')        
    ax1[1].hist([i for i in Pnemy0[0] if i >= 5],bins=256);
    ax1[1].grid(True)

    ax2[0].set_title('X-ray - Pneumonia with Infiltration (Average)')        
    ax2[0].hist([i for i in Pnemy1[1] if i >= 5],bins=256);
    ax2[0].grid(True)

    ax2[1].set_title('X-ray - Infiltration (Average)')        
    ax2[1].hist([i for i in Pnemy0[1] if i >= 5],bins=256);
    ax2[1].grid(True)

    ax3[0].set_title('X-ray - Pneumonia with Atelectasis (Average)')        
    ax3[0].hist([i for i in Pnemy1[2] if i >= 5],bins=256);
    ax3[0].grid(True) 

    ax3[1].set_title('X-ray - Atelectasis (Average)')        
    ax3[1].hist([i for i in Pnemy0[2] if i >= 5],bins=256);
    ax3[1].grid(True)

    ax4[0].set_title('X-ray - Pneumonia with Effusion (Average)')    
    ax4[0].hist([i for i in Pnemy1[3] if i >= 5],bins=256);
    ax4[0].grid(True)

    ax4[1].set_title('X-ray - Effusion (Average)')        
    ax4[1].hist([i for i in Pnemy0[3] if i >= 5],bins=256);
    ax4[1].grid(True) 
   
    