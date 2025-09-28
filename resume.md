title: Heungsub Lee · Résumé
description: The résumé of Heungsub Lee, a software engineer

Heungsub Lee
============

Contact {: .label }
: [heungsub@subl.ee](mailto:heungsub@subl.ee)
  {: .attr }

Web Sites {: .label }
: [subl.ee](/),
  [github.com/sublee](https://github.com/sublee),
  [linkedin.com/in/sublee](https://linkedin.com/in/sublee)
  {: .attr }

---

Interest
--------

Problem solving, AI services and platforms, real-time communication in
distributed systems, cost and performance optimization, and developer
experience.

Skills
------

Programming Languages {: .label }
: Go, Python, TypeScript
  {: .attr }

Service Development {: .label }
: Linux, AWS, gRPC, React, Pulumi, Kubernetes, Redis, PostgreSQL, ZeroMQ, OAuth,
  Concurrent programming, Testing
  {: .attr }

AI Engineering {: .label }
: MCP, PyTorch, NCCL, NVIDIA Nsight Systems
  {: .attr }

---

Work Experience
---------------

Lead Software Engineer {: .label }
[Global AI Platform][gapco], Sep 2023 -- Present
:   Leading the development of [Aster][], a personal AI agent service that helps
    users solve problems by planning task sequences and suggesting alternatives,
    integrating data and functions from multiple MCP servers.

    Directed [LangDiff][], an open-source library bridging structured LLM
    outputs with progressive UI rendering, which hid model latency and improved
    responsiveness, enabling a smoother Aster experience.

[gapco]: https://globalaiplatform.com/
[aster]: https://asterapp.ai/
[langdiff]: https://github.com/globalaiplatform/langdiff

Software Engineering Manager {: .label }
[NAVER][], Aug 2020 -- Jul 2023
:   Supervised 25 engineers on MLOps platforms to boost inference performance by
    2-3x and improve developer productivity for [HyperCLOVA][], a Korean-focused
    LLM.

    Developed [NSMLv2][], a large-scale ML research platform at CLOVA. Designed
    a multi-tenant, economics-driven architecture that enabled diverse
    organizations to share GPU clusters efficiently, reducing idle time and
    maximizing utilization. This platform institutionalized distributed training
    to address growing demand for scalable training workflows.

[naver]: https://navercorp.com/
[hyperclova]: https://clova.ai/hyperclova
[nsmlv2]: https://deview.kr/2023/sessions/550
[clova]: https://clova.ai/

Software Engineer {: .label }
[Kakao Brain][kakaobrain], Dec 2018 -- Aug 2020
:   Developed [torchgpipe][], an open-source pipeline parallelism library for
    PyTorch that scaled large AI models across multiple GPUs with minimal code
    changes and low overhead.

    Developed a serverless training framework and distributed hyperparameter
    search pipelines on an on-premise GPU cluster, improving resource
    utilization and automation for model training.

[kakaobrain]: https://github.com/kakaobrain
[torchgpipe]: https://torchgpipe.readthedocs.io/

Game Server Engineer {: .label }
[NEXON][], Mar 2011 -- Dec 2018
:   Developed cloud-native distributed MMORPG servers for Durango using
    pub/sub over a spatial grid system, supporting up to 70k concurrent users
    per game world.

    Developed online racing game servers and matchmaking for KartRider Dash and
    KartRider Coin Rush.

[nexon]: https://company.nexon.com/en/
[kartrider]: https://kart.nexon.com/

Back-end Web Developer {: .label }
[nPine][iclickart], Dec 2008 -- Feb 2011
:   Developed e-commerce web services for stock image platforms.

[iclickart]: https://iclickart.co.kr/

Open Source Experience
----------------------

[torchgpipe][], Feb 2019 -- Apr 2020
:   Implemented [GPipe][], a multi-GPU pipeline parallelism technique for
    large-scale model training, as a PyTorch library with CUDA, autograd, and
    long skip connection optimizations; later upstreamed into PyTorch as the
    official [Pipe APIs][pytorch-pipe].

[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965
[pytorch-pipe]: https://pytorch.org/docs/2.0/pipeline.html

[Hangulize][], Oct 2010 -- Present
:   Designed a Hangul transcription algorithm and released it as a free web
    tool widely used by professional Korean translators.

[hangulize]: https://hangulize.org/

[TrueSkill][trueskill], Jan 2012 -- Dec 2015
:   Implemented [TrueSkill™][trueskill-tm], the rating algorithm behind Xbox
    Live, as a Python library; presented at [PyData Berlin 2019][pydata2019].

[trueskill]: https://trueskill.org/
[trueskill-tm]: https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/
[pydata2019]: https://docs.google.com/presentation/d/1S5v9D31vpsr22efMSSCO6hmN2SQNCIqKG7JyGzUSzeI/edit?usp=sharing

Contributions
:   Contributed upstream patches improving GPU safety ([#27371][pytorch#27371])
    and API consistency ([#21006][pytorch#21006], [#25985][pytorch#25985]) in
    [PyTorch][]. Fixed subdomain URL bug ([#108][flask#108]) in [Flask][].

[pytorch]:       https://pytorch.org/
[pytorch#27371]: https://github.com/pytorch/pytorch/pull/27371
[pytorch#21006]: https://github.com/pytorch/pytorch/pull/21006
[pytorch#25985]: https://github.com/pytorch/pytorch/pull/25985
[pytorch#18568]: https://github.com/pytorch/pytorch/pull/18568
[flask]:         https://flask.palletsprojects.com/
[flask#108]:     https://github.com/pallets/flask/issues/108

---

Publications
------------

<!-- IEEE style: https://libguides.nps.edu/citation/ieee -->
- H. Park et al., "HPCClusterScape: Increasing Transparency and Efficiency of
  Shared High-Performance Computing Clusters for Large-scale AI Models,"
  [arXiv:2310.02120][arxiv:hpcclusterscape], Oct 2024.
- B. Kim et al., "What changes can large-scale language models bring? Intensive
  study on HyperCLOVA: Billions-scale Korean generative pretrained
  Transformers," [arXiv:2109.04650][arxiv:hyperclova], Sep 2021.
- C. Kim\*, Heungsub Lee\* et al., "torchgpipe: On-the-fly pipeline parallelism
  for training giant models," [arXiv:2004.09910][arxiv:torchgpipe], Apr 2020.

\*Contributed equally
{: .footnote }

*[B. Kim]: Boseop Kim
*[C. Kim]: Chiheon Kim

[arxiv:hpcclusterscape]: https://arxiv.org/abs/2310.02120
[arxiv:hyperclova]: https://arxiv.org/abs/2109.04650
[arxiv:torchgpipe]: https://arxiv.org/abs/2004.09910

Public Speeches
---------------

<!-- Also, IEEE style -->
- "NSML, the hyper-scale ML training platform," [KRnet, Jun 2022][krnet22].
- "[Remake of Hangulize][gokr1808]," Golang Korea Meetup, Aug 2018.
- "[Profiling][pycon15]," PyCon Korea, Aug 2015.
- "The server architecture of Durango," NDC, [2014][ndc14], [2016][ndc16], and
  [2018][ndc18].

[krnet22]: https://www.kca.kr/boardView.do?boardId=NOTICE&seq=4600077

[gokr1808]: https://subl.ee/~gokr1808
[pycon15]:  https://subl.ee/~pycon15

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

---

Languages
---------

- Korean --- Native
- English --- Conversant in reading and writing

Education
---------

Computer Software, [Kwangwoon University][kw], 2008, Completed the first year
only.

[kw]: https://www.kw.ac.kr/

<!-- abbrs -->
*[AWS]:    Amazon Web Services
*[NCCL]:   NVIDIA Collective Communications Library
*[AI]:     Artificial intelligence
*[ML]:     Machine learning
*[HPC]:    High-performance computing
*[MMORPG]: Massively multiplayer online role-playing game
*[NDC]:    NEXON Developers Conference
*[Ajax]:   Asynchronous JavaScript and XML
*[MCP]:    Model Context Protocol
