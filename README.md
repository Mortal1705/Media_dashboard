# 🎨Media Dashboard

## 📊 Overview
A **Dark Futuristic Neon Glassmorphism** themed streaming media analytics dashboard featuring advanced data visualization with interactive charts, real-time filtering, and powerful export capabilities.

## ✨ Key Features

### 🎨 Dark Futuristic Design
- **Glassmorphism UI**: Translucent panels with backdrop blur effects and neon borders
- **Neon Color Palette**: 
  - Primary Cyan: `#00F0FF` (borders, highlights, primary text)
  - Secondary Purple: `#D042FF` (accents, gradients, secondary elements)
  - Accent Blue: `#2A75FF` (buttons, interactive elements)
  - Neon Green: `#39ff14` (data labels on charts)
- **Gradient Text Effects**: CSS gradient text with `-webkit-background-clip` for modern typography
- **Animated Elements**: Smooth transitions, pulse effects, rotating backgrounds, shine effects on tabs
- **Custom Scrollbar**: Gradient scrollbar matching the theme

### 📊 Data Processing & Analytics
- **Multi-Platform Aggregation**: 22,998 streaming titles from 4 major platforms
- **High-Performance Processing**: Pandas-based data pipeline with efficient indexing
- **Real-time Filtering**: Multi-parameter filter system with validation
- **Actor Deep Search**: Advanced search with partial name matching

### 📈 Interactive Visualizations
- **Chart.js Integration**: 8 dynamic charts with Chart.js + DataLabels plugin v2
- **Real-time Data Labels**: All values visible without hover (neon green `#39ff14`)
- **Chart Types**:
  - Horizontal Bar Charts (Platform Distribution)
  - Doughnut Charts (Content Type with percentage display)
  - Vertical Bar Charts (Genres, Ratings)
  - Line Charts (Yearly trends, Career timeline)

### 💾 Export Capabilities
- **📸 PNG Image Export**: Download any chart as high-quality PNG using Canvas API
- **📊 Excel Export**: Export actor filmography tables as `.xlsx` files using SheetJS v0.18.5
- **One-Click Downloads**: Instant file generation with descriptive filenames

## 🎯 Dashboard Sections

### 🔥 SYSTEM OVERVIEW
**Advanced Filter Panel:**
- Platform selector: Netflix, Amazon Prime, Disney+, Hulu
- Content Type: Movie / TV Show
- Date Range: Start Date & End Date with validation
- Apply Filter button with cyberpunk styling

**KPI Card:**
- Total System Entries counter with animated numbers
- Gradient text effect (Cyan → Purple)
- Pulsing glow animation

**5 Interactive Charts:**
1. 🌐 **Platform Distribution Matrix** (Horizontal Bar + Data Labels)
2. 📁 **Content Type Analysis** (Doughnut + Percentages in legend)
3. 🎭 **Top 10 Genre Dominance** (Vertical Bar + Data Labels)
4. 🔒 **Rating Classification** (Vertical Bar + Data Labels)
5. 📈 **Yearly Content Evolution Timeline** (Line Chart + Area Fill)

### 👤 ACTOR ANALYTICS
**Actor Profile Scanner:**
- Search input with cyberpunk styling
- Real-time search with Enter key support

**Profile Display:**
- Actor name in gradient text (uppercase)
- Total Works KPI badge with gradient background
- Career statistics

**3 Specialized Charts:**
1. 🌐 **Platform Presence** (Vertical Bar Chart)
2. 🎭 **Specialty Genres** (Horizontal Bar Chart)
3. 📈 **Career Evolution Timeline** (Line Chart with filled area)

**Recent Works Table:**
- Top 10 filmography with glassmorphism styling
- Hover effects with neon glow
- Excel export button

## 🛠️ Tech Stack

### Backend
- **Python 3.12**: Core language
- **Flask**: Web framework & routing
- **Pandas**: Data processing & aggregation
- **Flask-CORS**: Cross-origin resource sharing

### Frontend
- **HTML5**: Semantic markup
- **Tailwind CSS (CDN)**: Utility-first CSS framework with custom config
- **Vanilla JavaScript (ES6+)**: No framework dependencies
- **Chart.js v4**: Interactive chart library
- **Chart.js DataLabels Plugin v2**: Data label annotations
- **SheetJS (xlsx v0.18.5)**: Excel file generation

### Fonts
- **Inter**: Body text (300-900 weights)
- **Orbitron**: Cyberpunk headers (400, 700, 900 weights)

### Deployment
- **Flask Development Server**: Port 5000 (local)
- **ngrok**: Optional online sharing

## 📈 Chart Features

### Data Label System
- **Always Visible**: No hover required to see values
- **Neon Green Styling**: `#39ff14` color with bold font
- **Smart Positioning**: Auto-aligned (top/right/end)
- **Number Formatting**: Comma separators (1,250)

### Export System
- **Chart Images**: Canvas API → PNG download
- **Excel Tables**: SheetJS → `.xlsx` generation
- **Filenames**: Descriptive naming (e.g., `platform_distribution_chart.png`)

### Chart Types Detail
- **Horizontal Bar**: Platform distribution with right-aligned labels
- **Doughnut**: Content type split with numbers inside + % in legend
- **Vertical Bar**: Genres/ratings with top-aligned labels
- **Line**: Temporal data with point markers and area fill

## 🎨 Visual Design System

### Glassmorphism Components
```css
background: rgba(20, 26, 38, 0.65);
backdrop-filter: blur(12px);
border: 1px solid rgba(0, 240, 255, 0.25);
border-radius: 16px;
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
```

### Gradient Text
```css
background: linear-gradient(135deg, #00F0FF 0%, #D042FF 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

### Button Effects
- **Gradient Background**: Purple → Blue
- **Ripple Effect**: Expanding circle on hover
- **Neon Glow**: Multi-layer box shadows
- **Transform**: Scale + translateY on hover

### Animations
- **Pulse**: KPI numbers breathing effect (2s loop)
- **Shine**: Light sweep across active tabs (3s loop)
- **Rotate**: Background gradient rotation (10s loop)
- **Bounce**: Loading indicators

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Mortal1705/Media_dashboard.git
cd Media_dashboard
```
2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run tests & Start Flask server
```bash
python3 run_tests.py
python3 app.py
```
Access the dashboard at: http://localhost:5000
### 🌐 Share Online Access via ngrok (Optional)
Open new terminal window:
```bash
ngrok http 5000
```
Copy the URL from the Forwarding section (e.g., https://3821-2001-ee0-4cc8-3b30-ff2d-7292-de6a-414e.ngrok-free.app) to share the Dashboard online.
## 📁 Project Structure
```
Media_dashboard/
├── app.py                      # Flask backend API & routing
├── run_tests.py                # Unit test execution script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (EN + VI)
├── .gitignore                  # Git ignore configuration
├── data/
│   ├── processed/
│   │   └── final_cleaned.csv  # Cleaned dataset (22,998 entries)
│   └── raw/
│       ├── amazon_prime_titles.csv
│       ├── disney_plus_titles.csv
│       ├── hulu_titles.csv
│       └── netflix_titles.csv
├── notebooks/
│   └── processed.ipynb         # Data cleaning 
├── templates/
│   └── index.html              # Dashboard frontend (HTML/CSS/JS)
└── test/
    ├── __init__.py             # Test package init
    ├── README.md               # Test documentation
    └── test_app.py             # API & data integrity tests (45+ cases)
```

## 🔧 API Endpoints

### Core Endpoints
- **`GET /`**: Serve main dashboard interface
- **`GET /api/filter`**: Advanced filtering with multiple parameters
- **`GET /api/dashboard/overview`**: System-wide analytics and charts data
- **`GET /api/dashboard/actor?name={actor_name}`**: Actor-specific analysis

### Filter Parameters
- `platform`: Netflix, Amazon Prime, Disney+, Hulu
- `type`: Movie, TV Show
- `start_date`, `end_date`: Date range filtering
- `cast`: Actor name search
- `rating`, `genre`, `country`: Content filtering
- `release_year`: Year-specific filtering

## 🎯 Browser Compatibility
- Modern browsers with Canvas API support
- JavaScript ES6+ features utilized
- CDN-based dependencies for reliability
- Responsive design for mobile/tablet devices

# 🎨 Dashboard Phân tích Dữ liệu Streaming Media

## 📊 Tổng quan
Dashboard phân tích dữ liệu Media với theme **Dark Futuristic Neon Glassmorphism**, tích hợp biểu đồ tương tác, lọc theo thời gian và khả năng xuất dữ liệu mạnh mẽ.

## ✨ Tính năng chính

### 🎨 Thiết kế Dark Futuristic
- **Glassmorphism UI**: Các panel trong suốt với hiệu ứng làm mờ nền và viền neon
- **Bảng màu Neon**: 
  - Cyan chính: `#00F0FF` (viền, highlight, text chính)
  - Tím phụ: `#D042FF` (điểm nhấn, gradient, element phụ)
  - Xanh dương: `#2A75FF` (nút, element tương tác)
  - Xanh neon: `#39ff14` (nhãn dữ liệu trên biểu đồ)
- **Hiệu ứng Gradient Text**: CSS gradient text với `-webkit-background-clip` cho typography hiện đại
- **Element Hoạt hình**: Transitions mượt, hiệu ứng pulse, background xoay, shine effect trên tabs
- **Scrollbar Tùy chỉnh**: Scrollbar gradient khớp với theme

### 📊 Xử lý & Phân tích Dữ liệu
- **Tích hợp Đa nền tảng**: 22,998 titles từ 4 nền tảng streaming lớn
- **Xử lý Hiệu suất Cao**: Pipeline dữ liệu Pandas với indexing hiệu quả
- **Lọc Thời gian thực**: Hệ thống lọc đa tham số với validation
- **Tìm kiếm Diễn viên Sâu**: Tìm kiếm nâng cao với khớp tên một phần

### 📈 Trực quan hóa Tương tác
- **Tích hợp Chart.js**: 8 biểu đồ động với Chart.js + DataLabels plugin v2
- **Nhãn Dữ liệu Thời gian thực**: Tất cả giá trị hiển thị không cần hover (xanh neon `#39ff14`)
- **Các loại Biểu đồ**:
  - Biểu đồ cột ngang (Phân phối Platform)
  - Biểu đồ tròn (Loại nội dung với hiển thị phần trăm)
  - Biểu đồ cột đứng (Thể loại, Xếp hạng)
  - Biểu đồ đường (Xu hướng hàng năm, Timeline sự nghiệp)

### 💾 Khả năng Xuất dữ liệu
- **📸 Xuất PNG**: Tải xuống biểu đồ dạng PNG chất lượng cao qua Canvas API
- **📊 Xuất Excel**: Xuất bảng filmography diễn viên dạng `.xlsx` qua SheetJS v0.18.5
- **Tải xuống Một chạm**: Tạo file ngay lập tức với tên mô tả

## 🎯 Các phần Dashboard

### 🔥 TỔNG QUAN HỆ THỐNG
**Bảng Lọc Nâng cao:**
- Chọn platform: Netflix, Amazon Prime, Disney+, Hulu
- Loại nội dung: Movie / TV Show
- Khoảng thời gian: Start Date & End Date với validation
- Nút Apply Filter với styling cyberpunk

**Thẻ KPI:**
- Bộ đếm Total System Entries với số hoạt hình
- Hiệu ứng gradient text (Cyan → Purple)
- Animation phát sáng nhấp nháy

**5 Biểu đồ Tương tác:**
1. 🌐 **Ma trận Phân phối Platform** (Cột ngang + Nhãn dữ liệu)
2. 📁 **Phân tích Loại Nội dung** (Tròn + Phần trăm trong legend)
3. 🎭 **Top 10 Thể loại Thống trị** (Cột đứng + Nhãn dữ liệu)
4. 🔒 **Phân loại Xếp hạng** (Cột đứng + Nhãn dữ liệu)
5. 📈 **Timeline Tiến hóa Nội dung Hàng năm** (Đường + Area fill)

### 👤 PHÂN TÍCH DIỄN VIÊN
**Máy quét Hồ sơ Diễn viên:**
- Ô tìm kiếm với styling cyberpunk
- Tìm kiếm thời gian thực với hỗ trợ phím Enter

**Hiển thị Hồ sơ:**
- Tên diễn viên với gradient text (IN HOA)
- Badge KPI Total Works với background gradient
- Thống kê sự nghiệp

**3 Biểu đồ Chuyên biệt:**
1. 🌐 **Hiện diện Platform** (Biểu đồ cột đứng)
2. 🎭 **Thể loại Chuyên môn** (Biểu đồ cột ngang)
3. 📈 **Timeline Tiến hóa Sự nghiệp** (Biểu đồ đường với area fill)

**Bảng Tác phẩm Gần đây:**
- Top 10 filmography với styling glassmorphism
- Hiệu ứng hover với neon glow
- Nút xuất Excel

## 🛠️ Ngăn xếp Công nghệ

### Backend
- **Python 3.12**: Ngôn ngữ lõi
- **Flask**: Web framework & routing
- **Pandas**: Xử lý & tổng hợp dữ liệu
- **Flask-CORS**: Chia sẻ tài nguyên cross-origin

### Frontend
- **HTML5**: Semantic markup
- **Tailwind CSS (CDN)**: CSS framework utility-first với config tùy chỉnh
- **Vanilla JavaScript (ES6+)**: Không phụ thuộc framework
- **Chart.js v4**: Thư viện biểu đồ tương tác
- **Chart.js DataLabels Plugin v2**: Chú thích nhãn dữ liệu
- **SheetJS (xlsx v0.18.5)**: Tạo file Excel

### Fonts
- **Inter**: Text body (độ đậm 300-900)
- **Orbitron**: Header cyberpunk (độ đậm 400, 700, 900)

### Triển khai
- **Flask Development Server**: Port 5000 (local)
- **ngrok**: Chia sẻ online (tùy chọn)

## 📈 Tính năng Biểu đồ

### Hệ thống Nhãn Dữ liệu
- **Luôn Hiển thị**: Không cần hover để xem giá trị
- **Styling Neon Green**: Màu `#39ff14` với font đậm
- **Định vị Thông minh**: Tự động căn chỉnh (trên/phải/cuối)
- **Định dạng Số**: Dấu phẩy ngăn cách (1,250)

### Hệ thống Xuất
- **Hình ảnh Biểu đồ**: Canvas API → Tải PNG
- **Bảng Excel**: SheetJS → Tạo `.xlsx`
- **Tên file**: Đặt tên mô tả (VD: `platform_distribution_chart.png`)

### Chi tiết Loại Biểu đồ
- **Cột ngang**: Phân phối platform với nhãn căn phải
- **Tròn**: Chia loại nội dung với số bên trong + % trong legend
- **Cột đứng**: Thể loại/xếp hạng với nhãn căn trên
- **Đường**: Dữ liệu thời gian với điểm đánh dấu và area fill

## 🎨 Hệ thống Thiết kế Trực quan

### Component Glassmorphism
```css
background: rgba(20, 26, 38, 0.65);
backdrop-filter: blur(12px);
border: 1px solid rgba(0, 240, 255, 0.25);
border-radius: 16px;
box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
```

### Gradient Text
```css
background: linear-gradient(135deg, #00F0FF 0%, #D042FF 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```

### Hiệu ứng Button
- **Gradient Background**: Tím → Xanh
- **Ripple Effect**: Vòng tròn mở rộng khi hover
- **Neon Glow**: Box shadows nhiều lớp
- **Transform**: Scale + translateY khi hover

### Animations
- **Pulse**: Hiệu ứng thở của số KPI (vòng lặp 2s)
- **Shine**: Ánh sáng quét qua tabs active (vòng lặp 3s)
- **Rotate**: Xoay gradient background (vòng lặp 10s)
- **Bounce**: Chỉ báo loading

## 🚀 Bắt đầu Nhanh
### 1. tải repository về máy (Clone)
```bash
git clone https://github.com/Mortal1705/Media_dashboard.git
cd Media_dashboard
```
2. tạo và kích hoạt môi trường ảo (Virtual environment)
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3.Cài đặt thư viện
```bash
pip install -r requirements.txt
```
4. Chạy kiểm tra và khởi động sever Flask
```bash
python3 run_tests.py
python3 app.py
```
Truy cập giao diện dashboard tại dường dẫn : http://localhost:5000 (Local)

### 🌐 Chia sẻ truy cập Online qua ngrok
mở cửa sổ terminal mới:
```bash
ngrok http 5000
```
Copy đường dẫn ở mục Forwarding (ví dụ: https://3821-2001-ee0-4cc8-3b30-ff2d-7292-de6a-414e.ngrok-free.app) để chia sẻ giao diện Dashboard trực tuyến.
## 📁 Cấu trúc Dự án

```
Media_dashboard/
├── app.py                      # Flask backend API & routing
├── run_tests.py                # Script thực thi unit test
├── requirements.txt            # Thư viện Python cần thiết
├── README.md                   # Tài liệu dự án (EN + VI)
├── .gitignore                  # Những file ko đẩy lên git
├── data/
│   ├── processed/
│   │   └── final_cleaned.csv  # Dataset đã làm sạch (22,998 entries)
│   └── raw/                    # Dữ liệu thô
│       ├── amazon_prime_titles.csv
│       ├── disney_plus_titles.csv
│       ├── hulu_titles.csv
│       └── netflix_titles.csv
├── notebooks/
│   └── processed.ipynb         # Notebook làm sạch dữ liệu 
├── templates/
│   └── index.html              # Frontend Dashboard (HTML/CSS/JS)
└── test/
    ├── __init__.py             # Khởi tạo package test
    ├── README.md               # Tài liệu test
    └── test_app.py             # Test API & tính toàn vẹn dữ liệu (45+ cases)
```

## 🔧 API Endpoints

### Endpoints Chính
- **`GET /`**: Phục vụ giao diện dashboard chính
- **`GET /api/filter`**: Lọc nâng cao với nhiều tham số
- **`GET /api/dashboard/overview`**: Phân tích toàn hệ thống và dữ liệu biểu đồ
- **`GET /api/dashboard/actor?name={actor_name}`**: Phân tích cụ thể diễn viên

### Tham số Lọc
- `platform`: Netflix, Amazon Prime, Disney+, Hulu
- `type`: Movie, TV Show
- `start_date`, `end_date`: Lọc theo khoảng thời gian
- `cast`: Tìm kiếm tên diễn viên
- `rating`, `genre`, `country`: Lọc nội dung
- `release_year`: Lọc theo năm cụ thể

## 🎯 Tương thích Trình duyệt
- Trình duyệt hiện đại với hỗ trợ Canvas API
- Sử dụng tính năng JavaScript ES6+
- Dependencies dựa trên CDN để đảm bảo độ tin cậy
- Thiết kế responsive cho thiết bị di động/tablet