Title: Résumé: Heungsub Lee

Heungsub Lee
============

Contact {: .label }
: [heungsub.lee@subl.ee](mailto:heungsub.lee@subl.ee)
  or
  [+82 10-3215-2380](sms:821032152380)
  {: .attr }

Web Sites {: .label }
: [Homepage](/),
  [GitHub Profile](https://github.com/sublee),
  [LinkedIn Profile](https://linkedin.com/in/sublee)
  {: .attr }
{^ .attrs }

---

Interests
---------

- Parallel and distributed deep learning
- Developing and documenting API for engineers
- Free and open source software

Skills
------

Programming Languages {: .label }
: Python (expert), Go, JavaScript, Bash, C#
  {: .attr }

AI Research {: .label }
: PyTorch, NVIDIA Nsight Systems, Data/model/pipeline Parallelism
  {: .attr }

Back-end Development {: .label }
: Linux, AWS, Terraform, Docker, ZeroMQ, Redis, etcd, MySQL
  {: .attr }

Test Engineering {: .label }
: Testify, mypy, pytest, GitLab CI, Travis CI
  {: .attr }
{^ .attrs }

---

Work Experience
---------------

Software Engineer {: .label }
[Kakao Brain][kakaobrain], 2018--
:   A deep learning artificial intelligence laboratory in Kakao.
    {: .note }

:   Focused on parallel and distributed deep learning to boost training
    performance.

    Reproduced [GPipe][] in PyTorch, and developed [torchgpipe][] as an open
    source library.

Game Server Architect {: .label }
What! Studio in [Nexon][], 2013--2018
:   Developing <cite>[Durango][]</cite>, a seamless open world MMORPG.
    {: .note }

:   Designed and implemented the architecture of a distributed MMORPG server.
    The server achieved up to 70k concurrent users per MMO world.

    Built an internationalization and localization system focused on
    linguistics features of Korean and Indo-European languages.

    Led the server development team including up to 15 game server engineers.

Game Development Engineer {: .label }
Team Lupin in [Nexon][], 2011--2013
:   Developed and launched multiplayer racing games: <cite>[KartRider][] Dash &
    Coin Rush</cite>
    {: .note }

:   Designed and implemented a distributed game server architecture for
    synchronous multiplayer racing games.

    Researched rating systems such as Elo, Glicko, and
    [TrueSkill][trueskill-tm] to develop a matchmaker for 4v4 or free-for-all
    games.

Full Stack Web Developer {: .label }
[Npine][], 2008--2011
:   Supplies stock images for business on <cite>[Iclickart][]</cite>.
    {: .note }

:   Developed web services from the base framework to the application.

    Maintained physical Linux machines in a data center.

    Led the software engineering team including three web developers.

Front-end Web Developer {: .label }
[Lunant][], 2008--2011
:   Served <cite>VLAAH</cite>, social media for discovering, sharing, and
    utilizing opinions.
    {: .note }

:   Designed and implemented the UI/UX for <cite>VLAAH</cite>.

    Developed an open source project [jDoctest][], which is a JavaScript
    testing framework using example code in documentation comments.

Open Source Experience
----------------------

[torchgpipe][], 2019--
:   A GPipe implementation in PyTorch.
    {: .note }

:   Implemented [GPipe][], which is a scalable pipeline parallelism library for
    training of a giant model, for PyTorch with a handy interface.

    Reproduced a ResNet-101 performance benchmark in the original GPipe paper.

[Hangulize][], 2010--
:   Automatically transcribes a non-Korean word into Hangul.
    {: .note }

:   Implemented an automatic Hangul transcription algorithm to realize
    [Brian Jongseong Park's idea] [hangulize-idea]. By origin, it was written
    in Python, but rewritten in Go for better features, performance, and
    productivity.

    Designed and implemented the web service and RESTful API. Many professional
    Korean translators usually visit here to translate undocumented proper
    nouns. For example, Ryu Gwang, who is a famous technical translator,
    introduced this web service in [his posting (Korean)][ryugwang].
    Furthermore, Netflix refers to it in [the Korean timed text style
    guide][netflix-style].

[TrueSkill][trueskill], 2012--
:   A TrueSkill™ implementation in Python.
    {: .note }

:   Implemented [TrueSkill™][trueskill-tm], which is a rating algorithm for
    Xbox Live, in Python with a handy interface to learn and popularize the
    algorithm.

[Profiling][], 2014--2018
:   An interactive profiler for Python inspired by the Unity3D profiler.
    {: .note }

:   Developed a tracing based and statistical profiler for Python with a handy
    interactive TUI like [htop][].

    2800+ people have stared this project on GitHub. Also, it was the 3rd daily
    trending repository on Sep 22, 2014.

Others
:   - [Tossi][] -- A utility for Korean allomorphic particles.
    - [SUBLEERUNKER][] -- A simple parody game of SUBERUNKER. Play it in your
                          web browser.
    - [Flask-AutoIndex][] -- mod_autoindex for Flask
    - [Me2virus][] -- An XSS attack on [Me2day][], social media. When a user
                      looks at an infected post, a new infected post was
                      written on the user's wall.

Contributions
:   [awesome-go#2104](https://github.com/avelino/awesome-go/pull/2104);
    [Babel#427](https://github.com/python-babel/babel/pull/427),
    [#488](https://github.com/python-babel/babel/pull/488);
    [base65536#2](https://github.com/Parkayun/base65536/pull/2);
    [couchbase-python-client#32](https://github.com/couchbase/couchbase-python-client/pull/32),
    [#33](https://github.com/couchbase/couchbase-python-client/pull/33),
    [#35](https://github.com/couchbase/couchbase-python-client/pull/35);
    [etcd#4320](https://github.com/coreos/etcd/pull/4320);
    [Flask-0.10.1](https://github.com/mitsuhiko/flask/commit/6fca662);
    [gevent#608](https://github.com/gevent/gevent/pull/608);
    [jQuery-1.4.3](https://blog.jquery.com/2010/10/16/jquery-143-released/);
    [node-irc#3](https://github.com/martynsmith/node-irc/pull/3);
    [pytest-rerunfailures#47](https://github.com/pytest-dev/pytest-rerunfailures/pull/47);
    [PyTorch#21006](https://github.com/pytorch/pytorch/pull/21006),
    [#21192](https://github.com/pytorch/pytorch/pull/21192);
    [PyZMQ#951](https://github.com/zeromq/pyzmq/pull/951);
    [TensorFlow#24678](https://github.com/tensorflow/tensorflow/pull/24678).

Public Speeches
---------------

- [Remake of Hangulize][gokr1808] at Golang Korea Meetup Aug 2018 (Korean)
- [The server architecture of Durango Vol. 3][ndc18] at NDC 2018 (Korean)
- [Python Survival Guide][nxtk16] at Nexon Talk 2016 (Korean)
- [The server architecture of Durango Vol. 2][ndc16] at NDC 2016,
  awarded the grand prize (Korean)
- [Profiling][pycon15] at PyCon KR 2015 (Korean)
- [The server architecture of Durango][ndc14] at NDC 2014 (Korean)

[ndc18]: https://subl.ee/~ndc18
[ndc16]: https://subl.ee/~ndc16
[ndc14]: https://subl.ee/~ndc14

[gokr1808]: https://subl.ee/~gokr1808
[nxtk16]:   https://subl.ee/~nxtk16
[pycon15]:  https://subl.ee/~pycon15

---

Languages
---------

- Korean -- native
- English -- conversational

Education
---------

Computer Software, [Kwangwoon University][kw], 2008
-- Completed the first year only.

<!-- links -->
[gpipe]: https://arxiv.org/abs/1811.06965
[torchgpipe]: https://github.com/kakaobrain/torchgpipe
[durango]: http://durango.nexon.com/
[flask-autoindex]: http://pythonhosted.org/Flask-AutoIndex
[hangulize-idea]: http://iceager.egloos.com/2610028
[hangulize]: https://hangulize.org/
[ryugwang]: http://occamsrazr.net/tt/351
[htop]: http://hisham.hm/htop
[iclickart]: http://iclickart.co.kr/
[jdoctest]: https://lunant.github.com/jdoctest
[kakaobrain]: https://kakaobrain.com/
[kartrider]: http://kart.nexon.com/
[kw]: http://www.kw.ac.kr/
[lunant]: http://lunant.net/
[me2day]: https://en.wikipedia.org/wiki/Me2day
[me2virus]: https://github.com/sublee/me2virus
[netflix-style]: https://partnerhelp.netflixstudios.com/hc/en-us/articles/216001127-Korean-Timed-Text-Style-Guide
[nexon]: https://company.nexon.com/eng
[npine]: http://en.npine.com/
[profiling]: https://github.com/what-studio/profiling
[subleerunker]: /runker/
[tossi]: https://github.com/what-studio/tossi
[trueskill]: https://trueskill.org/
[trueskill-tm]: http://research.microsoft.com/en-us/projects/trueskill/

<!-- abbrs -->
*[AWS]: Amazon Web Services
*[MMORPG]: Massively multiplayer online role-playing game
*[NDC]: Nexon Developers Conference
*[TUI]: Text-based User Interface
*[XSS]: Cross-site Scripting
