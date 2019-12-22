# project-1

Sử dụng SVM để dự đoán hướng chuyển động của thị trường tài chính
Yêu cầu: Máy tính có cài đặt Python 3.5 và các thư viện pandas,sklearn,matplotlib,joblib,numpy
Bước 1: Mở terminal chạy lệnh để sử lý dữ liệu raw tạo ra file trainningset.csv và testset.csv
	python processRawData.py
Bước 2: Sau khi thành công màn hình sẽ hiện thị ra 70 dữ liệu đầu tiên của tập dữ liệu, đóng cửa sổ chạy câu lệnh trainning mô hình
	python train.py
Bước 3: Đợi mô hình tranning xong sẽ tạo ra file clf.pkl lưu lại mô hình sau khi train và hiện thị mô hình đóng cửa sổ chạy câu lệnh test độ chính xác của mô hình
	python test.py
Sau khi hoàn thành terminal sẽ hiển thị độ chính xác của mô hình trên tập test.	