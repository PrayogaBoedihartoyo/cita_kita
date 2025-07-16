import pandas as pd
import json

def process_cities_csv():        
    try:
        print("📂 Membaca file cities.csv...")
        df = pd.read_csv('cities.csv')
        print(f"✅ Berhasil membaca {len(df)} baris data")
        
        print(f"📊 Kolom yang tersedia: {list(df.columns)}")
        print(f"🌍 Sample data:")
        print(df[['name', 'country_name']].head(3))
        print()
        
        print("🔄 Mengelompokkan kota berdasarkan negara...")
        country_counts = df.groupby('country_name').size().reset_index(name='jumlah_kota')
        
        country_counts = country_counts.sort_values('jumlah_kota', ascending=False)
        country_counts = country_counts.reset_index(drop=True)
        
        print(f"✅ Berhasil mengelompokkan {len(country_counts)} negara")
        print()
        
        print("🏆 TOP 10 NEGARA DENGAN KOTA TERBANYAK:")
        print("-" * 45)
        for i, row in country_counts.head(10).iterrows():
            print(f"{i+1:2d}. {row['country_name']:<25} : {row['jumlah_kota']:,} kota")
        print()
        
        total_cities = country_counts['jumlah_kota'].sum()
        total_countries = len(country_counts)
        avg_cities = total_cities / total_countries
        
        print("📈 STATISTIK:")
        print(f"   Total Negara    : {total_countries:,}")
        print(f"   Total Kota      : {total_cities:,}")
        print(f"   Rata-rata Kota  : {avg_cities:.1f}")
        print(f"   Negara Terbanyak: {country_counts.iloc[0]['country_name']} ({country_counts.iloc[0]['jumlah_kota']:,} kota)")
        print()
        
        print("💾 Menyimpan hasil...")
        country_counts.to_csv('output.csv', index=False)
        print("✅ Hasil disimpan dalam file: output.csv")
        
        result_json = country_counts.to_dict('records')
        with open('output.json', 'w') as f:
            json.dump(result_json, f, indent=2)
        print("✅ Hasil disimpan dalam file: output.json")
        
        print()
        print("🎉 PROSES SELESAI!")
        print("=" * 50)
        
        return country_counts
        
    except FileNotFoundError:
        print("❌ ERROR: File cities.csv tidak ditemukan!")
        print("   Pastikan file cities.csv ada di folder yang sama dengan script ini.")
        return None
    
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return None

def show_sample_results():
    try:
        df = pd.read_csv('output.csv')
        print("\n📋 PREVIEW HASIL (output.csv):")
        print("-" * 40)
        print(df.head(10).to_string(index=False))
        
        print("\n📋 PREVIEW HASIL (output.json):")
        print("-" * 40)
        with open('output.json', 'r') as f:
            data = json.load(f)
        for i, item in enumerate(data[:5]):
            print(f"{i+1}. {item['country_name']}: {item['jumlah_kota']} kota")
            
    except FileNotFoundError:
        print("📝 File output belum ada. Jalankan proses terlebih dahulu.")

if __name__ == "__main__":
    result = process_cities_csv()
    
    if result is not None:
        print("\n" + "=" * 50)
        show_sample_results()