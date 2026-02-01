@echo off
chcp 65001
echo 开始合并Excel表...
python simple_merger.py
echo.
echo 合并完成！请查看生成的"员工信息与绩效合并表.xlsx"文件
pause
