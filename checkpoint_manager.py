#!/usr/bin/env python3
"""
檢查點管理模塊 - 為小說生成任務提供狀態保存和恢復功能
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

REPO_PATH = Path(__file__).parent.parent
CHECKPOINT_DIR = REPO_PATH / "checkpoints"
ACTIVE_CHECKPOINT = CHECKPOINT_DIR / "active_novel-generation.json"

def save_checkpoint(step, progress, data, extra=""):
    """保存檢查點"""
    try:
        CHECKPOINT_DIR.mkdir(exist_ok=True)
        
        checkpoint = {
            "task_id": "novel-generation",
            "task_name": "novel-generation",
            "step": step,
            "progress": progress,
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "extra": extra,
            "hostname": os.uname().nodename if hasattr(os, 'uname') else "unknown",
            "working_dir": str(REPO_PATH)
        }
        
        with open(ACTIVE_CHECKPOINT, 'w', encoding='utf-8') as f:
            json.dump(checkpoint, f, indent=2, ensure_ascii=False)
        
        print(f"✅ 檢查點已保存: {step} ({progress}%)")
        return True
        
    except Exception as e:
        print(f"⚠️  檢查點保存失敗: {e}")
        return False

def load_checkpoint():
    """加載檢查點"""
    if not ACTIVE_CHECKPOINT.exists():
        return None
    
    try:
        with open(ACTIVE_CHECKPOINT, 'r', encoding='utf-8') as f:
            checkpoint = json.load(f)
        
        print(f"📋 發現檢查點: {checkpoint['step']} ({checkpoint['progress']}%)")
        print(f"   時間: {checkpoint['timestamp']}")
        return checkpoint
        
    except Exception as e:
        print(f"⚠️  檢查點加載失敗: {e}")
        return None

def clear_checkpoint():
    """清除活動檢查點（任務完成後）"""
    if ACTIVE_CHECKPOINT.exists():
        try:
            ACTIVE_CHECKPOINT.unlink()
            print("🧹 檢查點已清除")
            return True
        except Exception as e:
            print(f"⚠️  檢查點清除失敗: {e}")
            return False
    return True

def list_checkpoints():
    """列出所有檢查點"""
    try:
        checkpoints = list(CHECKPOINT_DIR.glob("*.json"))
        if not checkpoints:
            print("📭 沒有檢查點文件")
            return []
        
        print(f"📁 找到 {len(checkpoints)} 個檢查點:")
        for cp in sorted(checkpoints, key=lambda x: x.stat().st_mtime, reverse=True):
            try:
                with open(cp, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"   - {cp.name}: {data['step']} ({data['progress']}%) - {data['timestamp']}")
            except:
                print(f"   - {cp.name}: (無法讀取)")
        
        return checkpoints
    except Exception as e:
        print(f"❌ 列出檢查點失敗: {e}")
        return []

# 檢查點步驟常量
STEP_DETERMINE_CHAPTER = "determine-chapter"
STEP_API_CALL = "api-call"
STEP_EXTRACT_TITLE = "extract-title"
STEP_GENERATE_HTML = "generate-html"
STEP_UPDATE_NAV = "update-nav"
STEP_GIT_COMMIT = "git-commit"
STEP_COMPLETED = "completed"
STEP_ERROR = "error"
