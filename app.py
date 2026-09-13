import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, 'data', 'processed','final_cleaned.csv')
df = pd.read_csv(csv_path)

df['date_added'] = pd.to_datetime(df['date_added'])
# hàm nhận lấy tham số :
def get_params():
    return {
        'show_id': request.args.get('show_id'),
        'type': request.args.get('type'),                      
        'title': request.args.get('title'),                    
        'director': request.args.get('director'),
        'cast': request.args.get('cast'),                      
        'country': request.args.get('country'),
        'release_year': request.args.get('release_year'),      
        'rating': request.args.get('rating'),
        'duration': request.args.get('duration'),
        'listed_in': request.args.get('listed_in'),            
        'description': request.args.get('description'),        
        'platform': request.args.get('platform'),              
        'duration_int_min': request.args.get('duration_int_min'),  
        'duration_int_max': request.args.get('duration_int_max'),  
        'duration_unit': request.args.get('duration_unit'),    
        'start_date': request.args.get('start_date'),          
        'end_date': request.args.get('end_date')
    }
# hàm lọc tham số :
def filter_data(data_frame, **kwargs):
    filtered_df = data_frame.copy()
    
    str_contains_cols = ['title', 'director', 'cast', 'country', 'listed_in', 'description']
    for col in str_contains_cols: #lọc theo từ khóa gợi ý
        val = kwargs.get(col)
        if val:
            filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(val, case=False, na=False)]

    str_exact_cols = ['show_id', 'type', 'rating', 'platform', 'duration', 'duration_unit']
    for col in str_exact_cols: #lọc chính xác theo từ khóa 
        val = kwargs.get(col)
        if val:
            filtered_df = filtered_df[filtered_df[col].astype(str).str.lower() == str(val).lower()]

    # Lọc giá trị số
        if kwargs.get('release_year'):
            try:
                val = int(kwargs['release_year'])
                filtered_df = filtered_df[filtered_df['release_year'] == val]
            except(ValueError, TypeError):
                return jsonify({'error': 'release_year phải là một số nguyên hợp lệ.'}), 400
        if kwargs.get('duration_int_min'):
            try:
                val = float(kwargs['duration_int_min'])
                filtered_df = filtered_df[filtered_df['duration_int'] >= val]
            except(ValueError, TypeError):
                return jsonify({'error': 'duration_int_min phải là một số  hợp lệ.'}), 400         
        if kwargs.get('duration_int_max'):
            try:
                val = float(kwargs['duration_int_max'])
                filtered_df = filtered_df[filtered_df['duration_int'] <= val]
            except(ValueError, TypeError):
                return jsonify({'error': 'duration_int_max phải là một số  hợp lệ.'}), 400

   # Lọc khoảng thời gian (date_added)
    try:
        if kwargs.get('start_date'):
            filtered_df = filtered_df[filtered_df['date_added'] >= pd.to_datetime(kwargs['start_date'])]
        if kwargs.get('end_date'):
            filtered_df = filtered_df[filtered_df['date_added'] <= pd.to_datetime(kwargs['end_date'])]
    except (ValueError, TypeError, pd.errors.ParserError):
        raise jsonify({'error': 'Định dạng ngày tháng không hợp lệ.'})

    return filtered_df
@app.route('/')
def home():
    return render_template('index.html') 
@app.route('/api/filter', methods=['GET'])
def filter_titles():
    params = get_params()
    try:
        filtered_df = filter_data(df, **params)
    except Exception as e:
        # Bắt lỗi khi người dùng truyền tham số sai (như định dạng ngày tháng)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
  
    # Chuyển đổi datetime thành string YYYY-MM-DD
    results = filtered_df.copy()
    results['date_added'] = results['date_added'].dt.strftime('%Y-%m-%d')
    
    return jsonify({
        'status': 'success',
        'total_results': len(filtered_df),
        'data': results.to_dict(orient='records')
    })

@app.route('/api/dashboard/overview', methods=['GET'])
def get_dashboard_overview():
    params = get_params()
    filtered_df = filter_data(df, **params)

    # 1. Tỷ lệ theo plaform (vẻ biểu đồ cột ngang)
    platforms = filtered_df['platform'].value_counts()
    chart_platform = {
        'labels': platforms.index.tolist(),
        'values': platforms.values.tolist()
    }

    # 2. Tỷ lệ theo Type (Vẽ biểu đồ tròn)
    types = filtered_df['type'].value_counts()
    chart_type = {
        'labels': types.index.tolist(),
        'values': types.values.tolist()
    }

    # 3. Top 10 Thể loại (Vẽ biểu đồ cột đứng)
    genres = filtered_df['listed_in'].dropna().str.split(', ').explode()
    top_genres = genres.value_counts().head(10)
    chart_genres = {
        'labels': top_genres.index.tolist(),
        'values': top_genres.values.tolist()
    }
    # 4. Phân bố phim theo Xếp loại độ tuổi (Rating - Bar Chart)
    ratings = filtered_df['rating'].value_counts().head(10)
    chart_ratings = {
        'labels': ratings.index.tolist(),
        'values': ratings.values.tolist()
    }
    # 5. Số lượng phim bổ sung hằng năm
    trends = filtered_df['date_added'].dt.year.value_counts().sort_index()
    chart_trends = {
        'labels': trends.index.tolist(), 
        'values': trends.values.tolist()
    }
    
    return jsonify({
        'status': 'success',
        'total_titles': len(filtered_df),
        'charts': {
            'platform_distribution': chart_platform, 
            'type_distribution': chart_type,         
            'top_genres': chart_genres,
            'rating_distribution': chart_ratings,
            'trends': chart_trends,
        }
    })
  
@app.route('/api/dashboard/actor', methods=['GET'])
def get_actor_overview():
    # Lấy tên diễn viên từ param 'name' hoặc 'cast'
    actor_name = request.args.get('name') or request.args.get('cast')
    
    if not actor_name:
        return jsonify({
            'status': 'error',
            'message': 'Vui lòng cung cấp tên diễn viên (param: name hoặc cast)'
        }), 400

    # Lọc các bộ phim có sự tham gia của diễn viên (tìm kiếm chứa tên)
    actor_df = filter_data(df, cast=actor_name)

    if actor_df.empty:
        return jsonify({
            'status': 'success',
            'actor': actor_name,
            'total_works': 0,
            'message': 'Không tìm thấy dữ liệu cho diễn viên này'
        })

    # 1. Thống kê Nền tảng (Platform)
    platform_counts = actor_df['platform'].value_counts()
    chart_platforms = {
        'labels': platform_counts.index.tolist(),
        'values': platform_counts.values.tolist()
    }

    # 2. Thống kê Thể loại sở trường (Top Genres)
    genres = actor_df['listed_in'].dropna().str.split(', ').explode()
    top_genres = genres.value_counts().head(5)
    chart_genres = {
        'labels': top_genres.index.tolist(),
        'values': top_genres.values.tolist()
    }

    # 3. Xu hướng hoạt động theo năm (Release Year)
    trends = actor_df['release_year'].value_counts().sort_index()
    chart_trends = {
        'labels': trends.index.tolist(),
        'values': trends.values.tolist()
    }

    # 4. Danh sách Top 10 phim mới nhất của diễn viên
    top_movies = actor_df.sort_values('release_year', ascending=False).head(10)[
        ['title', 'type', 'release_year', 'platform', 'listed_in']
    ].to_dict(orient='records')

    return jsonify({
        'status': 'success',
        'actor': actor_name,
        'total_works': len(actor_df),
        'charts': {
            'platform_distribution': chart_platforms, # Biểu đồ tròn/Cột
            'top_genres': chart_genres,                # Biểu đồ cột
            'career_timeline': chart_trends            # Biểu đồ đường (Line Chart)
        },
        'recent_works': top_movies
    })

if __name__ == '__main__':
    app.run(debug = True, port = 5000)
