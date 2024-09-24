# Copyright (c) Meta Platforms, Inc. and affiliates
# All rights reserved.
#
# This source code is licensed under the license found in the
# MIT_LICENSE file in the root directory of this source tree.


from .streaming.agents.detokenizer import UnitYDetokenizerAgent
from .streaming.agents.offline_w2v_bert_encoder import (
    OfflineWav2VecBertEncoderAgent,
)
from .streaming.agents.online_feature_extractor import (
    OnlineFeatureExtractorAgent,
)
from .streaming.agents.online_text_decoder import (
    UnitYMMATextDecoderAgent,
)
from .streaming.agents.online_unit_decoder import (
    NARUnitYUnitDecoderAgent,
)
from .streaming.agents.pretssel_vocoder import (
    PretsselVocoderAgent,
)
from .streaming.agents.dual_vocoder_agent import (
    DualVocoderAgent,
)
from .streaming.agents.silero_vad import SileroVADAgent
from .streaming.agents.unity_pipeline import (
    UnitYAgentPipeline,
    UnitYAgentTreePipeline,
)


class SeamlessS2STAgent(UnitYAgentPipeline):
    pipeline = [
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        UnitYMMATextDecoderAgent,
        NARUnitYUnitDecoderAgent,
        PretsselVocoderAgent,
    ]


class SeamlessS2STJointVADAgent(UnitYAgentTreePipeline):
    pipeline = {
        SileroVADAgent: [OnlineFeatureExtractorAgent],
        OnlineFeatureExtractorAgent: [OfflineWav2VecBertEncoderAgent],
        OfflineWav2VecBertEncoderAgent: [UnitYMMATextDecoderAgent],
        UnitYMMATextDecoderAgent: [UnitYDetokenizerAgent, NARUnitYUnitDecoderAgent],
        UnitYDetokenizerAgent: [],
        NARUnitYUnitDecoderAgent: [PretsselVocoderAgent],
        PretsselVocoderAgent: [],
    }


class SeamlessS2STDualVocoderVADAgent(UnitYAgentTreePipeline):
    pipeline = {
        SileroVADAgent: [OnlineFeatureExtractorAgent],
        OnlineFeatureExtractorAgent: [OfflineWav2VecBertEncoderAgent],
        OfflineWav2VecBertEncoderAgent: [UnitYMMATextDecoderAgent],
        UnitYMMATextDecoderAgent: [UnitYDetokenizerAgent, NARUnitYUnitDecoderAgent],
        UnitYDetokenizerAgent: [],
        NARUnitYUnitDecoderAgent: [DualVocoderAgent],
        DualVocoderAgent: [],
    }
