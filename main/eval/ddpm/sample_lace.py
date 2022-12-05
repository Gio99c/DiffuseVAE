import os
import sys

p = os.path.join(os.path.abspath("."), "main")
sys.path.insert(1, p)

import hydra
from eval.ddpm.sample_cond import sample_cond

@hydra.main(config_path=os.path.join(p, "configs"))
def sample_lace(config):
    sample_cond(config)


if __name__ == "__main__":
    sample_lace()