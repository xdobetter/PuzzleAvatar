import numpy as np


if __name__ == "__main__":


    data_root = "./data/PuzzleIOI/fitting"
    results_path = "./results/PuzzleIOI/results.npy"

    all_outfits = np.loadtxt("clusters/subjects_all.txt", dtype=str, delimiter=" ")[:,0]
    all_outfits = [f"./data/{outfit}/" for outfit in all_outfits]

    results = np.load(results_path, allow_pickle=True).item()

    total_names = []
    total_metrics = {"Chamfer": [], "P2S": [], "Normal": [], "PSNR": [], "SSIM": [], "LPIPS": []}

    for subject in results.keys():
        for outfit in results[subject].keys():
            total_names.append(f"{subject}_{outfit}")
            for key in total_metrics.keys():
                total_metrics[key].append(results[subject][outfit][key])
                
                
    topk=100
    good_chamfer = [total_names[idx] for idx in np.argsort(total_metrics["Chamfer"])[:topk]]
    good_psnr = [total_names[idx] for idx in np.argsort(total_metrics["LPIPS"])[-topk:]]
    
    print(np.intersect1d(good_chamfer, good_psnr))
