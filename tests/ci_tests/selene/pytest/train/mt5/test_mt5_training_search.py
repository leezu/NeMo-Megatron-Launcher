import os


BASE_RESULTS_DIR = os.environ.get("BASE_RESULTS_DIR")
RUN_SIZE = os.environ.get("RUN_SIZE")
GPU_MEM = os.environ.get("GPU_MEM")
NODES = os.environ.get("NODES")

class TestCImT5:

    def test_ci_train_mt5(self):
        base_cfg = os.path.join(BASE_RESULTS_DIR, f"mt5/{RUN_SIZE}_{GPU_MEM}gb/base_cfg_{RUN_SIZE}.yaml")
        candidate_configs_dir = os.path.join(BASE_RESULTS_DIR, f"mt5/{RUN_SIZE}_{GPU_MEM}gb/candidate_configs")
        training_logs_dir = os.path.join(BASE_RESULTS_DIR, f"mt5/{RUN_SIZE}_{GPU_MEM}gb/training_logs")
        final_result_dir = os.path.join(BASE_RESULTS_DIR, f"mt5/{RUN_SIZE}_{GPU_MEM}gb/final_result")
        final_summary_csv = os.path.join(BASE_RESULTS_DIR, f"mt5/{RUN_SIZE}_{GPU_MEM}gb/final_result/final_summary_{NODES}nodes.csv")
        optimal_cfg = os.path.join(BASE_RESULTS_DIR, f"mt5/{RUN_SIZE}_{GPU_MEM}gb/final_result/optimal_config_{RUN_SIZE}_{NODES}nodes.yaml")

        assert os.path.exists(base_cfg), f"File not found: {base_cfg}"
        assert os.path.exists(candidate_configs_dir), f"Dir not found: {candidate_configs_dir}"
        assert os.path.exists(training_logs_dir), f"Dir not found: {training_logs_dir}"
        assert os.path.exists(final_result_dir), f"Dir not found: {final_result_dir}"
        assert os.path.exists(final_summary_csv), f"File not found: {final_summary_csv}"
        assert os.path.exists(optimal_cfg), f"File not found: {optimal_cfg}"
