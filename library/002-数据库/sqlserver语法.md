## sqlserver语法

给表中添加字段

```sql
ALTER TABLE 表名 ADD 列名 数据类型 [约束];
```

示例

1. 添加单列

```sql
ALTER TABLE Products ADD Description NVARCHAR(500) NULL;
```

2. 添加带默认值的列

   ```sql
   ALTER TABLE Orders ADD OrderDate DATE NOT NULL DEFAULT GETDATE();
   ```

3. 添加带约束的列

   ```SQL
   ALTER TABLE Employees ADD Salary DECIMAL(10,2) NOT NULL CHECK (Salary > 1000);
   ```

4. 添加多列

   ```sql
   ALTER TABLE Inventory ADD LastStockDate DATETIME,RestockLevel INT NOT NULL DEFAULT 50;
   ```

   

**注意**

1. **数据类型必须有效**：如 `INT`, `VARCHAR(n)`, `DATETIME`, `DECIMAL(p,s)` 等
2. **NULL/NOT NULL 约束**：
   - 新列默认允许 NULL（除非指定 NOT NULL）
   - 添加 NOT NULL 列时必须：
     - 有 DEFAULT 约束
     - 或表为空
3. **默认值**：
   - 使用 `DEFAULT` 关键字设置初始值
   - 系统函数如 `GETDATE()` 可用于动态值
4. **并发操作**：
   - 大表添加列可能锁表，建议在低峰期操作
   - 使用 `WITH (ONLINE = ON)` 减少阻塞（企业版功能）



**验证结果**

```sql
-- 查看表结构
EXEC sp_columns 'Users';
```

**删除列语法**

```sql
ALTER TABLE 表名 DROP COLUMN 列名;
```



**重要提示：**生产环境修改表结构前，请务必：

1. 备份数据库
2. 在测试环境验证
3. 使用事务（BEGIN TRAN...ROLLBACK）测试

