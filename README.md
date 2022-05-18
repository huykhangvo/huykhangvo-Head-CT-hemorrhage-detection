
## Học máy - Dự án cuối cùng

![dataset-cover](https://user-images.githubusercontent.com/44756354/88648428-a697df00-d0cf-11ea-979e-7010b14c7fa9.jpg)
# CT đầu phát hiện xuất huyết

### Giới thiệu:
Trong dự án này, chúng tôi đã sử dụng các thuật toán học máy khác nhau để phân loại hình ảnh. Chúng tôi đã làm việc với [CT đầu xuất huyết](https://www.kaggle.com/felipekitamura/head-ct-hemorrhage/?select=head_ct) tập dữ liệu, chứa 100 lát cắt CT đầu bình thường và 100 lát cắt khác có xuất huyết.

### Yêu cầu
* Python 3.6+
* NumPy (pip install numpy)
* Pandas (pip install pandas)
* OpenCv (pip install opencv-python)
* Scikit-learn (pip install scikit-learn)
* SciPy (pip install scipy)
* glob (pip install glob)
* MatplotLib (pip install matplotlib)
* Tensorflow (pip install tensorflow)
* Keras (pip install keras)
### Về dự án:
Chúng tôi đã kiểm tra kết quả của các bộ phân loại sau:
* KNN - with the euclidean distance
* KNN - with earth mover distance
* SVM - with linear, polynomial, RBF, sigmoid kernel.  
* ADABOOST
* DECISION TREE
* RANDOM FOREST
* CNN - Convolutional neural network

## Ví dụ:
![both](https://user-images.githubusercontent.com/44756354/88721518-3faa1280-d12f-11ea-8ddb-9ed9ba3aa8d2.png)


## Thực hiện:
- **Khai thác tính năng**: 

Đầu tiên, chúng tôi trích xuất các tính năng bằng hai cách tiếp cận:

  1) Đơn giản - Sử dụng OpenCV để thay đổi kích thước hình ảnh thành kích thước nhỏ hơn và sau đó đẩy hình ảnh sang mảng một chiều với các pixel của hình ảnh.
  
  2) Biểu đồ - Biểu đồ màu là một biểu diễn của sự phân bố màu sắc trong một hình ảnh. Đối với hình ảnh kỹ thuật số, biểu đồ màu biểu thị số lượng pixel có màu trong mỗi danh sách dải màu cố định, trải dài không gian màu của hình ảnh, tập hợp tất cả các màu có thể có. Sau đó, chúng tôi xáo trộn và chia nhỏ dữ liệu thành trainX, trainY, testX, testY và gửi đến bộ phân loại
  
- **Phân loại**:
    
    húng tôi gửi dữ liệu đến bộ phân loại và mỗi bộ phân loại đều làm những việc tương tự: huấn luyện dữ liệu (phù hợp), lấy điểm của máy và dự đoán của máy trên một trong các hình ảnh trong tập dữ liệu.
    
Đối với CNN, chúng tôi sử dụng cách tiếp cận Đơn giản để trích xuất các tính năng và chúng tôi thay đổi kích thước hình ảnh ở kích thước 320X320, sau đó chúng tôi xáo trộn và chia nhỏ dữ liệu. Sau đó, chúng tôi xây dựng một mô hình với 5 lớp chập, và sau đó chúng tôi đào tạo mô hình.
    
## Độ chính xác (Hiệu suất):

   ![Accuracy](https://user-images.githubusercontent.com/44756354/88837833-58730080-d1e1-11ea-8ea1-e31953694850.png)
   ![AccuracyCNN](https://user-images.githubusercontent.com/44756354/88838146-cd463a80-d1e1-11ea-89a0-956b01683913.png)

## Sự kết luận

   Như chúng ta có thể thấy, phương pháp Đơn giản có kết quả tốt hơn sau đó là Biểu đồ, vì chúng tôi có độ chính xác 90% về knn và độ chính xác 85% trong rừng ngẫu nhiên.
   
   Nhưng như chúng tôi nghĩ, mạng nơ-ron liên kết là cách tiếp cận tốt nhất để phân loại hình ảnh và thực sự chúng tôi đã đạt được độ chính xác 100% khi sử dụng nó để phân loại hình ảnh.


## Người đóng góp

* [Roi Abramovitch](https://www.linkedin.com/in/roi-abramovitch-04b62821/)

* [Chen Asaraf](https://www.linkedin.com/in/chen-asaraf/)
