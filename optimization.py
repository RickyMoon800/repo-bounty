import asyncio
import logging
import time

# 配置日志，确保生产环境可追溯
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def process_task(task_id: int):
    """
    具体的业务处理函数：
    在真实的 Bounty 中，这里填入数据清洗/API 请求逻辑。
    """
    logger.info(f"[Task {task_id}] 正在处理...")
    await asyncio.sleep(0.5) # 模拟 IO 开销
    logger.info(f"[Task {task_id}] 处理成功")
    return {"id": task_id, "status": "success"}

async def main():
    """
    核心优化：使用 asyncio.gather 实现高并发 IO
    """
    total_tasks = 10
    tasks = [process_task(i) for i in range(total_tasks)]

    start_time = time.perf_counter()
    logger.info(f"开始批量处理 {total_tasks} 个任务...")

    # 真正的并发执行点
    results = await asyncio.gather(*tasks)

    end_time = time.perf_counter()
    logger.info(f"任务完成，耗时: {end_time - start_time:.2f} 秒")
    logger.info(f"结果摘要: {results[:2]} ... 等")

if __name__ == '__main__':
    # 确保正常退出
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
