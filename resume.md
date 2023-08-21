title: Résumé: Heungsub Lee
description: A résumé of Heungsub Lee, a software engineer

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

Interests
---------

- Software for software engineers or researchers
- Distributed system and cloud-native back-end development
- Parallelism in machine learning
- Cost optimization and management for systems top on GPUs

Skills
------

Programming Languages {: .label }
: Go, Python, TypeScript, JavaScript, Bash
  {: .attr }

ML Engineering {: .label }
: PyTorch, pipeline parallelism, NVIDIA Nsight Systems
  {: .attr }

Back-end Development {: .label }
: Linux, K8s, AWS, Terraform, MySQL, MongoDB, Couchbase, Redis, etcd, ZeroMQ
  {: .attr }

---

Work Experience
---------------

Software Engineering Manager {: .label }
[CLOVA][] in [NAVER][] and [NAVER Cloud][], 2020--2023
:   Develops hyperscale AI-based products.
    {: .note }

:   Led 25 MLOps software engineers focusing on data pipelining, model
    training platforms, model serving platforms, GPU resource management, and
    inference optimization for [HyperCLOVA][], an LLM specializing in Korean
    culture.

    Developed the second version of [NSML][], an ML research platform on HPC
    infrastructures focused on large-scale AI models.

[clova]: https://clova.ai/
[naver]: https://navercorp.com/en
[naver cloud]: https://navercloudcorp.com/lang/en
[hyperclova]: https://arxiv.org/abs/2109.04650
[nsml]: https://arxiv.org/abs/1712.05902

Software Engineer {: .label }
[Kakao Brain][kakaobrain], 2018--2020
:   An AI research subsidiary of Kakao
    {: .note }

:   Focused on parallel training of convolutional neural networks, including
    large-scale data parallelism and pipeline parallelism. Developed and
    published a pipeline parallelism library in PyTorch named [torchgpipe][].

    Developed a serverless training framework and a distributed hyperparameter
    search platform for an AutoML service.

[kakaobrain]: https://kakaobrain.com/
[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965

Game Server Engineer {: .label }
[NEXON][], 2011--2018
:   Develops and publishes online video games.
    {: .note }

:   Developed cloud-based distributed game servers for Durango (MMORPG) that
    communicate with each other by pub/sub over the spatial grid system.
    This game achieved up to 70k concurrent users per game world.

    Developed online racing game servers for [KartRider][] Dash and KartRider
    Coin Rush. Researched rating algorithms such as Elo, Glicko, and
    [TrueSkill&trade;][trueskill-tm] for matchmaking in those games.

    Led 15 game server engineers.

[nexon]: https://company.nexon.com/en/
[kartrider]: https://kart.nexon.com/
[trueskill-tm]: https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/

Web Developer {: .label }
nPine, 2008--2011
:   Supplies stock images for business on [Iclickart][].
    {: .note }

:   Developed web services from scratch. Maintained on-premise Linux servers.

[iclickart]: https://iclickart.co.kr/

Front-end Web Developer {: .label }
[Lunant][], 2008--2011
:   Served social media named VLAAH.
    {: .note }

:   Designed and implemented the UI/UX for social media.

[lunant]: https://github.com/lunant

Open Source Experience
----------------------

[torchgpipe][], 2019--2020
:   A GPipe implementation in PyTorch
    {: .note }

:   Implemented [GPipe][] in PyTorch with optimization for CUDA, PyTorch's
    autograd engine, and long skip connections. GPipe is a scalable pipeline
    parallelism library for the training of a giant model.

    This project has become a part of PyTorch as [Pipe APIs][pytorch-pipe]. The
    story behind it can be found on [Kakao Brain
    Blog<sup>ko</sup>][torchgpipe-blog] and [the technical
    report][arxiv:torchgpipe].

[torchgpipe]: https://torchgpipe.readthedocs.io/
[gpipe]: https://arxiv.org/abs/1811.06965
[torchgpipe-blog]: https://web.archive.org/web/20211020112459/https://kakaobrain.com/blog/66
[pytorch-pipe]: https://pytorch.org/docs/2.0/pipeline.html
[arxiv:torchgpipe]: https://arxiv.org/abs/2004.09910

[Hangulize][], 2010--
:   Transcribes a non-Korean word into Hangul.
    {: .note }

:   Implemented an automatic Hangul transcription algorithm to realize [Brian
    Jongseong Park's idea][hangulize-idea]. Developed the algorithm and the web
    service.

    Many professional Korean translators habitually use this tool to translate
    undocumented proper nouns. Netflix refers to this tool in [the Korean
    timed-text style guide][netflix-style].

[hangulize]: https://hangulize.org/
[hangulize-idea]: https://web.archive.org/web/20230616001454/https://iceager.egloos.com/2610028
[netflix-style]: https://partnerhelp.netflixstudios.com/hc/en-us/articles/216001127-Korean-Timed-Text-Style-Guide

[TrueSkill][trueskill], 2012--2015
:   A TrueSkill™ implementation in Python
    {: .note }

:   Implemented [TrueSkill™][trueskill-tm], which is a rating algorithm for
    Xbox Live, in Python with a handy interface. This project was introduced in
    [PyData Berlin 2019][pydata2019].

[trueskill]: https://trueskill.org/
[trueskill-tm]: https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/
[pydata2019]: https://docs.google.com/presentation/d/1S5v9D31vpsr22efMSSCO6hmN2SQNCIqKG7JyGzUSzeI/edit?usp=sharing

[Profiling][], 2014--2018
:   An interactive profiler for Python inspired by the Unity3D profiler
    {: .note }

:   Developed a Python profiler with an interactive TUI inspired by [the Unity
    profiler][unity-profiler]. On GitHub, this project has been starred by 3k
    people. Also, it was the 3rd daily trending repository on Sep 22, 2014.

[profiling]: https://github.com/what-studio/profiling
[unity-profiler]: https://docs.unity3d.com/Manual/ProfilerWindow.html

Others
:   - [Tossi][] -- A utility for Korean allomorphic particles
    - [Flask-AutoIndex][] -- mod_autoindex for [Flask][]
    - [SUBLEERUNKER][] -- A simple parody game of SUBERUNKER

[tossi]: https://github.com/what-studio/tossi
[flask-autoindex]: https://flask-autoindex.readthedocs.io/
[flask]: https://flask.palletsprojects.com/
[subleerunker]: /runker/

Contributions
:   - For [PyTorch][],
      fixed potential GPU memory violation ([#27371][pytorch#27371]);
      deprecated inconsistent API ([#21006][pytorch#21006],
      [#25985][pytorch#25985]); discussed a counterintuitive behavior
      of the autograd engine ([#18568][pytorch#18568]).
    - For [ZeroMQ][],
      discussed a PUB socket crash ([#2942][zeromq#2942]).
    - For [Flask][],
      fixed a bug to generate a URL with a subdomain ([#108][flask#108]).
    - For [jQuery 1.4.3][jquery-143],
      fixed content negotiation in Ajax requests.

[pytorch]:       https://pytorch.org/
[pytorch#27371]: https://github.com/pytorch/pytorch/pull/27371
[pytorch#21006]: https://github.com/pytorch/pytorch/pull/21006
[pytorch#25985]: https://github.com/pytorch/pytorch/pull/25985
[pytorch#18568]: https://github.com/pytorch/pytorch/pull/18568
[zeromq]:        https://zeromq.org/
[zeromq#2942]:   https://github.com/zeromq/libzmq/issues/2942
[flask]:         https://flask.palletsprojects.com/
[flask#108]:     https://github.com/pallets/flask/issues/108
[jquery-143]:    https://blog.jquery.com/2010/10/16/jquery-143-released/

---

Publications
------------

- B. Kim et al., "What Changes Can Large-scale Language Models Bring? Intensive
  Study on HyperCLOVA: Billions-scale Korean Generative Pretrained
  Transformers," [arXiv:2109.04650][arxiv:hyperclova], Sep 2021.
- C. Kim\*, _H. Lee_\*, M. Jeong, W. Baek, B. Yoon, I. Kim, S. Lim, S. Kim,
  "torchgpipe: On-the-fly Pipeline Parallelism for Training Giant Models,"
  [arXiv:2004.09910][arxiv:torchgpipe], Apr 2020.

*[B. Kim]:   Boseop Kim
[arxiv:hyperclova]: https://arxiv.org/abs/2109.04650

*[C. Kim]:   Chiheon Kim
*[H. Lee]:   Heungsub Lee
*[M. Jeong]: Myungryong Jeong
*[W. Baek]:  Woonhyuk Baek
*[B. Yoon]:  Boogeon Yoon
*[I. Kim]:   Ildoo Kim
*[S. Lim]:   Sungbin Lim
*[S. Kim]:   Sungwoong Kim
[arxiv:torchgpipe]: https://arxiv.org/abs/2004.09910

\*Contributed equally
{: .footnote }

Public Speeches
---------------

- NSML the hyper-scale ML training platform at [KRnet 2022][krnet]
- [Remake of Hangulize<sup>ko</sup>][gokr1808] at Golang Korea 2018 and NAVER D2
- [Server architecture of Durango Vol. 3<sup>ko</sup>][ndc18] at NDC 2018
- [Python Survival Guide<sup>ko</sup>][nxtk16] at NEXON Talk 2016
- [Server architecture of Durango Vol. 2<sup>ko</sup>][ndc16] at NDC 2016
- [Profiling<sup>ko</sup>][pycon15] at PyCon KR 2015
- [Server architecture of Durango<sup>ko</sup>][ndc14] at NDC 2014

[krnet]: https://www.kca.kr/boardView.do?boardId=NOTICE&seq=4600077

[gokr1808]: https://subl.ee/~gokr1808
[nxtk16]:   https://subl.ee/~nxtk16
[pycon15]:  https://subl.ee/~pycon15

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

---

Languages
---------

- Korean -- native
- English -- conversant in reading and writing

Education
---------

Computer Software, [Kwangwoon University][kw], 2008
-- completed the first year only

[kw]: https://www.kw.ac.kr/

<!-- abbrs -->
*[K8s]:    Kubernetes
*[AWS]:    Amazon Web Services
*[AI]:     Artificial intelligence
*[ML]:     Machine learning
*[HPC]:    High-performance computing
*[LLM]:    Large language model
*[MMORPG]: Massively multiplayer online role-playing game
*[NDC]:    NEXON Developers Conference
*[TUI]:    Text-based user interface
*[Ajax]:   Asynchronous JavaScript and XML
