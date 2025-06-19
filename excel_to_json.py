import pandas as pd
import json

excel_file = "商品清冊.xlsx"  # ← Excel 檔案名稱（跟 .py 放在同一資料夾）
output_file = "products.json"

df = pd.read_excel(excel_file, sheet_name=0, header=0)

product_db = {}

for index, row in df.iterrows():
    barcode = str(row[0]).strip()  # A欄 條碼
    name = str(row[1]).strip()     # B欄 品名
    tax_type = int(row[22]) if pd.notna(row[22]) else 0  # W欄 稅別
    try:
        price = float(str(row[15]).replace(",", ""))  # P欄 定價
    except:
        price = 0

    if barcode:
        product_db[barcode] = {
            "name": name,
            "taxType": tax_type,
            "price": round(price)
        }

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(product_db, f, ensure_ascii=False, indent=2)

print(f"✅ 共轉出 {len(product_db)} 筆商品，已儲存到 {output_file}")
