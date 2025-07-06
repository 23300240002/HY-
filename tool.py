# 安装：pip install pymupdf
import fitz  # pymupdf

def downgrade_pdf(input_path, output_path):
    doc = fitz.open(input_path)
    
    # 设置PDF版本为1.4 (对应Acrobat 5)
    doc.save(
        output_path,
        garbage=4,  # 清理无用对象
        deflate=True,  # 使用deflate压缩
        clean=True,  # 清理内容
        pdf_version="1.4"  # 设置为PDF 1.4版本
    )
    print(f"已将PDF降级为1.4版本并保存到 {output_path}")
    doc.close()

# 使用示例
downgrade_pdf("HY回忆录.pdf", "HY.pdf")