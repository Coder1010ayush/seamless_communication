# Copyright (c) Meta Platforms, Inc. and affiliates
# All rights reserved.
#
# This source code is licensed under the license found in the
# MIT_LICENSE file in the root directory of this source tree.

from .streaming.agents.detokenizer import DetokenizerAgent
from .streaming.agents.offline_w2v_bert_encoder import (
    OfflineWav2VecBertEncoderAgent,
)
from .streaming.agents.online_feature_extractor import (
    OnlineFeatureExtractorAgent,
)
from .streaming.agents.online_text_decoder import (
    MMASpeechToTextDecoderAgent,
)
from .streaming.agents.silero_vad import SileroVADAgent
from .streaming.agents.unity_pipeline import UnitYAgentPipeline


class SeamlessStreamingS2TDetokAgent(UnitYAgentPipeline):
    pipeline = [
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        MMASpeechToTextDecoderAgent,
        DetokenizerAgent,
    ]


class SeamlessStreamingS2TAgent(UnitYAgentPipeline):
    pipeline = [
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        MMASpeechToTextDecoderAgent,
    ]


class SeamlessStreamingS2TVADAgent(UnitYAgentPipeline):
    pipeline = [
        SileroVADAgent,
        OnlineFeatureExtractorAgent,
        OfflineWav2VecBertEncoderAgent,
        MMASpeechToTextDecoderAgent,
        DetokenizerAgent,
    ]
