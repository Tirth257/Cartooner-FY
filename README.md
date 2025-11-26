# Cartooner-FY
# **TikkhaX – Making Images into Cartoons**

## **Project Title:**  
### **Making Images to Cartoons (Image Color Segmentation using Python)**

## **Team Name:**  
**TikkhaX**

## **Authors / Team Members:**  
- Tirth Patel - BC2025103
- Namya Mankad - BC2025066
- Dhyan Patel - BC2025072

---

## **Short Description**  
This project focuses on transforming normal images into a cartoon-like representation using Python.  
By applying a **threshold-based color segmentation algorithm**, the program groups pixels based on RGB similarity and replaces each group with its average color.  
The final output looks smoother, simpler, and more stylized—similar to cartoon illustrations.

---

## **Concepts Used**
- RGB Image Processing
- Threshold‑based Segmentation  
- Use of Data Structures: Sets, Arrays  
- Functional Programming (Lambda)  
- Tkinter GUI for file selection  
- Numpy numerical operations 
- Matplotlib for visual output  
---

## **Libraries Used**
- `PIL (Pillow)` – loading and converting images  
- `numpy` – pixel matrix manipulation  
- `math` – Euclidean distance calculation  
- `matplotlib.pyplot` – displaying output  
- `tkinter` – file dialogs  
- `sys` – program exits  

---

## **Main Components of the Program**

### **1. Image Loading (AskFile)**
- Opens a dialog to select an image

### **2. Region Growing (Run)**
- Picks an unprocessed pixel  
- Calculates color distance  
- If distance < threshold → added to region  
- Region average color updates  
- All region pixels become same color  

### **3. Display Output**
Matplotlib shows the final cartoonified image.

---

## **Input and Output**

### **Input:**  
Any standard image file selected through the file dialog.

### **Output:**  
A cartoon-like version of the image displayed in a window.

---

## **Project File Structure**
```
/src
    cartoonify.py
/docs
    README.md
/data
    (sample images)
```

---

## **Setup & How to Run**

### **1. Install Dependencies**
```
pip install pillow numpy matplotlib
```

### **2. Run the Program**
```
python cartoonify.py
```

### **3. Steps**
1. Select an image  
2. Enter threshold  
3. Choose algorithm  
4. View cartoon result  

---

## **Notes**
- Works best with colorful input images  
- Higher threshold → fewer colors → bold cartoon effect
---

