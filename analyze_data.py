import json
from pathlib import Path
from datetime import datetime

def analyze_paper_counts():
    daily_dir = Path("data/daily")
    
    if not daily_dir.exists():
        print("No daily data found")
        return
    
    daily_files = sorted(daily_dir.glob("*.json"), reverse=True)
    
    print("📊 论文数量统计 - 最近10天：")
    print("-" * 50)
    
    total_papers = 0
    count_data = []
    
    for daily_file in daily_files[:15]:  # 查看最近15天的数据
        with open(daily_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        count = len(data)
        total_papers += count
        date_str = daily_file.stem
        
        count_data.append((date_str, count))
        print(f"📅 {date_str}: {count} 篇论文")
    
    print("-" * 50)
    
    # 计算平均值和中位数
    if count_data:
        counts = [c for _, c in count_data]
        avg_count = sum(counts) / len(counts)
        max_count = max(counts)
        min_count = min(counts)
        
        print(f"\n📈 统计摘要：")
        print(f"   最多一天：{max_count} 篇")
        print(f"   最少一天：{min_count} 篇")
        print(f"   平均每天：{avg_count:.1f} 篇")
        
        # 找到论文最多的日期
        max_date = next(date for date, count in count_data if count == max_count)
        print(f"   最多的日期：{max_date}")

if __name__ == "__main__":
    analyze_paper_counts()
