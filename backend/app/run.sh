#!/bin/bash

echo "initialize process running..."
cd /app/backend/app/db && alembic upgrade head
allergies=(
    # 特定原材料（表示義務8品目）
    "えび" "かに" "くるみ" "小麦" "そば" "卵" "乳" "落花生"
    # 特定原材料に準ずるもの（表示推奨20品目）
    "アーモンド" "あわび" "いか" "いくら" "オレンジ" "カシューナッツ" "キウイフルーツ" "牛肉" "ごま" 
    "さけ" "さば" "大豆" "鶏肉" "バナナ" "豚肉" "マカダミアナッツ" "もも" "やまいも" "りんご" "ゼラチン"
)

i=0
str=""
for a in "${allergies[@]}"
do
    let i++
    if [ -z "$str" ]; then
        str="($i, '$a')"
        continue
    fi
    str="$str, ($i, '$a')"
done

mysql -h"$DB_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "USE $MYSQL_DATABASE; INSERT IGNORE INTO allergy (allergy_id, name) VALUES $str;"

cd /app/backend/app && uvicorn main:app --reload --port=8080 --host=0.0.0.0