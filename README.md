# Quản lý chuyến bay

## Giới thiệu
### Đồ án Nhập môn Công nghệ phần mềm - Nhóm 13.
### Tên đề tài: Phần mềm quản lý chuyến bay
### Nội dung
Đề tài của nhóm là một trang web chuyên dùng để tìm kiếm và đặt vé chuyến bay cho khách hàng, đồng thời cung cấp cho doanh nghiệp khả năng quản lý hệ thống bán vé chuyến bay

### Nhóm 13:
|SID|Name|GitHub handle|
|---|----|-------------|
|19120338|Trần Hoàng Quân|[@trhgquan](https://github.com/trhgquan)|
|19120469|Sử Nhật Đăng|[@nhatdang2604](https://github.com/nhatdang2604)|
|19120542|Trần Cẩm Khánh|[@flauwa](https://github.com/flauwa)|
|19120598|Nguyễn Thị Kim Ngân|[@ntkngan1185](https://github.com/ntkngan1185)|
|19120682|Lê Hoàng Trọng Tín|[@nuno314](https://github.com/nuno314)|

## Tham khảo
### Backend
### Frontend
- [Trang chủ của Traveloka](https://www.traveloka.com)

## Môi trường cài đặt
- Hệ điều hành: Windows 7/8/10
- Ngôn ngữ lập trình: Python 3.x
- Framework sử dụng: Django
- Phiên bản framework: Django 4.0.4
- Database: PostgreSQL

## Cài đặt
### Install required packages
```
pip install -r requirements.txt
```

### Database migration
```
cd FlightManager
python manage.py migrate
```

### Chạy server
Browse vào thư mục FlightManager,
```
python runserver.py runserver
```

### Hướng dẫn deploy
#### Yêu cầu
- Người deploy đã cài đặt Heroku CLI
- Người deploy phải có một tài khoản [Github](https://www.github.com)
- Người deploy phải có một tài khoản [Heroku](https://www.heroku.com/)
- Tài khoản github này phải có 1 repository đã được push mã nguồn từ branch _staging_ ở repo này

#### Hướng dẫn
##### Bước 1: Tạo app
- Truy cập vào [Heroku](https://www.heroku.com/) và đăng nhập vào tài khoản đã tạo sẵn
- Nhấn vào nút _new_ để tạo một app mới trên __Heroku__
![markdown](deploy_tutorial/step_1.png)

- Chọn _Create new app_
![markdown](deploy_tutorial/step_2.png)

- Đặt tên, chọn region cho app, sau đấy nhấn nút _Create_
![markdown](deploy_tutorial/step_3.png)

- Ta được chuyển đến màn hình quản lý app
![markdown](deploy_tutorial/step_4.png)

##### Bước 2: Tạo Heroku PostgreSQL để sử dụng PostgreSQL
- Trên màn hình quản lý app, chọn _Resource_
![markdown](deploy_tutorial/step_5.png)

- Trên thanh tìm kiếm, hãy tìm keyword _Heroku Postgres_
![markdown](deploy_tutorial/step_6.png)

- Chọn phiên bản _Hobby Dev - Free_ và nhấn __Submit Order Form__
![markdown](deploy_tutorial/step_7.png)

##### Bước 3: Tiến hành deploy

- Trên navbar, chọn _Deploy_, kéo xuống phần __Deployment Method__ và chọn _Connect to GitHub_
![markdown](deploy_tutorial/step_8.png)