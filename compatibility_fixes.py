# compatibility_fixes.py
# Fixes for various compatibility issues in the RAG system

import numpy as np
import os

def apply_compatibility_fixes():
    """Apply all necessary compatibility fixes"""
    
    # Fix NumPy 2.0 compatibility
    if not hasattr(np, 'float_'):
        np.float_ = np.float64
    
    # Fix ChromaDB configuration for deployment
    os.environ['CHROMA_DB_IMPL'] = 'duckdb+parquet'
    os.environ['CHROMA_SERVER_HOST'] = 'localhost'
    os.environ['CHROMA_SERVER_HTTP_PORT'] = '8000'
    
    # Fix PyTorch device issues
    os.environ['CUDA_VISIBLE_DEVICES'] = ''  # Force CPU usage
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'  # Avoid tokenizer warnings
    
    # Fix SQLite compatibility
    try:
        import sys
        __import__('pysqlite3')
        sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
    except ImportError:
        pass  # pysqlite3 not available, use system sqlite3
    
    print("✅ Compatibility fixes applied successfully")

if __name__ == "__main__":
    apply_compatibility_fixes()
