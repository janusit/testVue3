from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import mysql.connector
from mysql.connector import Error

app = FastAPI()

# 数据库配置
db_config = {
    'host': 'hudi',
    'database': 'db_msg',
    'user': 'root',
    'password': '123456'
}

class QueryRequest(BaseModel):
    table: str
    fields: str
    condition: str

class AnalysisRequest(BaseModel):
    type: str
    field: str

@app.post("/api/query")
async def execute_query(query: QueryRequest):
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            query_str = f"SELECT {query.fields} FROM {query.table}"
            if query.condition:
                query_str += f" WHERE {query.condition}"
            
            cursor.execute(query_str)
            records = cursor.fetchall()
            return records
            
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.post("/api/analyze")
async def run_analysis(analysis: AnalysisRequest):
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            
            # 根据分析类型执行不同的SQL查询
            if analysis.type == 'count':
                query_str = f"SELECT COUNT({analysis.field}) as result FROM users"
            elif analysis.type == 'avg':
                query_str = f"SELECT AVG({analysis.field}) as result FROM users"
            elif analysis.type == 'sum':
                query_str = f"SELECT SUM({analysis.field}) as result FROM users"
            elif analysis.type == 'max':
                query_str = f"SELECT MAX({analysis.field}) as result FROM users"
            elif analysis.type == 'min':
                query_str = f"SELECT MIN({analysis.field}) as result FROM users"
            else:
                raise HTTPException(status_code=400, detail="不支持的分析类型")
            
            cursor.execute(query_str)
            result = cursor.fetchone()
            
            # 获取图表数据
            chart_query = "SELECT MONTH(created_at) as month, COUNT(*) as count FROM users GROUP BY MONTH(created_at)"
            cursor.execute(chart_query)
            chart_data = cursor.fetchall()
            
            labels = [f"{row['month']}月" for row in chart_data]
            values = [row['count'] for row in chart_data]
            
            return {
                'result': result['result'],
                'chartData': {
                    'labels': labels,
                    'values': values
                }
            }
            
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()  