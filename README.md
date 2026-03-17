# Auto Research Skills

把 `autoresearch` 里最值得迁移的那部分东西，从“自动训练实验”提炼成“通用 agent 研究循环”。

## 灵感来源

这个项目的灵感，直接来自 **Andrej Karpathy** 的开源项目 **`autoresearch`**：

- 项目名称：`autoresearch`
- 作者：Andrej Karpathy
- 仓库地址：<https://github.com/karpathy/autoresearch>

我们学习和借鉴的，不是它具体的训练代码实现，而是它背后那套非常有启发性的研究循环设计：

- 先定义 scorecard
- 先建立 baseline
- 再做小步实验
- 只在证据支持时 `keep`
- 把失败也写进日志
- 持续维护 frontier，而不是随机漂移

## 这个项目是什么

这是一个极小的开源项目，包含两个语言版本的 skill：

- `auto-research`
- `auto-research-zh`

它们的作用不是回答问题，而是把长周期、开放式、研究型、优化型任务组织成受约束的迭代循环。

换句话说，它们适合：

- 让 agent 连续优化一类流程
- 让 agent 逐轮推进一个不确定的问题
- 让 agent 在有指标和边界的前提下做探索

它们不适合：

- 一次性任务
- 没有衡量标准的任务
- 高风险、不可回退、不可审计的动作

## 我们为什么开源它

`autoresearch` 给我们的启发不是“AI 可以自己训练模型”，而是：

**探索型任务，终于可以被设计成一种更像研究组织的 agent loop。**

我们把这套方法抽成 skill，不是为了制造一个更大的叙事，而是想把几个最朴素但最有用的原则固定下来：

- evaluator 要稳定
- action surface 要收窄
- round 要足够小
- keep / discard 机制要明确
- frontier summary 要持续更新

如果这些东西没有写清楚，所谓“自主 agent”很容易退化成高成本随机游走。

这也是我们决定把它整理成 skill 的原因：

**相比一大段一次性的 prompt，skill 更适合沉淀这种可以被团队反复调用的 agent workflow。**

## 目录结构

```text
auto-research-skills/
├── README.md
├── README_EN.md
├── LICENSE
├── assets/
│   └── README.md
└── skills/
    ├── auto-research/
    └── auto-research-zh/
```

## 里面有什么

每个 skill 都包含：

- `SKILL.md`：触发条件、workflow、feedback loop、资源入口
- `references/loop-design.md`：完整方法论
- `references/templates.md`：scorecard、TSV 日志、handoff 模板
- `references/examples.md`：触发样例与重构样例
- `scripts/init_loop.py`：初始化研究工作区脚本

## 适合什么任务

### 1. Prompt 与 workflow 优化

不是一次性生成 20 个方案，而是让 agent 像研究员一样逐轮迭代、记录和比较。

### 2. 增长实验与内容实验

前提是你能定义清楚指标、预算和 guardrails。

### 3. 复杂自动化流程的稳定性改进

尤其适合“会反复坏、但每次坏得不完全一样”的流程。

### 4. 研究型工作

包括资料搜集、假设筛选、方向比较、frontier 压缩。

## 示意场景

下面这些是示意场景，不是客户案例。

### 场景一：把客服话术优化变成连续实验

不是让 agent 一次性生成很多话术，而是定义回复率、留资率、品牌边界，然后一轮只改一个变量，让话术像实验系统一样迭代。

### 场景二：把脆弱工作流越修越稳

把 success rate、failure mode、runtime 当成统一 evaluator，让 agent 每轮只修一个验证点，最后得到的是一条更稳定的流程，而不是一堆说不清为什么有效的 patch。

### 场景三：把“研究部”装进 agent loop

把资料采集、方向判断、frontier summary、假设队列这些动作流程化。人类不再负责盯所有细节，而是只在真正值得拍板的地方出手。

## 怎么用

最简单的方式，是把需要的 skill 目录复制到你的 agent skills 目录里，例如：

```text
.agents/skills/
└── auto-research/
```

或：

```text
.agents/skills/
└── auto-research-zh/
```

然后在合适的任务里显式调用，或者让系统根据 `description` 自动触发。

如果你要为一个新目标初始化研究工作区，可以直接运行：

```bash
python skills/auto-research/scripts/init_loop.py --name "your-objective"
```

或中文版：

```bash
python skills/auto-research-zh/scripts/init_loop.py --name "你的目标"
```

## 关于我们

我们是 **艾维禾砺数字科技有限公司**，专门帮助企业和个人把 AI 真正落到业务里。

我们不是只做单点开发，也不是传统意义上的“接需求就写代码”的外包团队。我们更关注的是，怎么把一个组织从“知道 AI 很重要”，带到“真的把 AI 用起来，并持续产生业务价值”。

我们做的是一条完整的陪跑式落地链路：

- 前期痛点发掘与场景判断
- 需求梳理与可行性评估
- 方案设计与实施路径规划
- AI 系统开发与企业现有系统集成
- 部署上线、持续运维与效果跟踪
- 后续迭代升级与人员培训

也就是说，我们做的不是“把功能做完就结束”，而是从前到后陪着把事情真正跑起来。

我们的主要业务包括：

- 企业 AI 咨询
- 定制化 AI 开发
- AI 技术培训

对我们来说，真正有价值的不是 demo，而是：

- 能上线
- 能接进业务
- 能被团队真正使用
- 能持续产生效果

## 我们在做什么

除了咨询、开发和培训，我们也在持续推进一套面向企业的 **数字员工平台**。

它的核心思路不是做一个会聊天的 demo，而是把企业级数字员工真正需要的基础设施补齐，比如：

- 面向岗位分化的 Agent Base
- 更清晰的工具接入与治理
- 权限控制与调用审计
- 统一交互层与多渠道接入
- 适合企业环境的持续运行方式

我们更关心的，不是“一个 agent 看起来多聪明”，而是：

**它能不能在真实业务里持续工作、可控运行、逐步放大价值。**

**对热点项目，真正有价值的反应不是转发，而是抽象、重构、开源。**

如果你也在做这些方向，尤其是：

- 企业 AI workflow
- 数字员工 / agent 平台
- OpenClaw 相关实践或二次开发
- 面向真实业务的 agent 落地

那这类问题我们大概率有共同语言。

## OpenClaw 相关支持

OpenClaw 是近期非常受关注的 agent 项目之一，我们也一直在持续跟进这类“从 demo 走向真实生产力”的技术方向。

围绕 OpenClaw 方向，我们可以提供的支持包括但不限于：

- OpenClaw 相关能力调研、技术方案梳理与落地方向判断
- 基于 OpenClaw 的企业场景适配与二次封装
- 围绕浏览器自动化、调试链路、实时会话能力的场景设计
- 结合具体业务流程的 agent workflow 设计与自动化编排
- 面向具体岗位或场景的 AI 员工 / AI 助理方案设计
- 与现有系统、知识库、数据源、内部流程的集成对接
- 围绕 OpenClaw 生态的咨询、交付与落地支持

如果你最近也在关注 OpenClaw，你会发现企业真正关心的通常不是“模型有多酷”，而是：

- 能不能接进现有流程
- 能不能真的节省人力
- 能不能降低试错门槛
- 能不能做成一个可持续使用的系统

这也是我们对 OpenClaw 这类项目最感兴趣的地方。

## 联系方式

- 官网：[official.ivheli.com](https://official.ivheli.com)
- 助理微信：`xmaiyrjgzs`

### 助理微信

![助理微信二维码](assets/wechat-qr.png)

### 公众号

![公众号二维码](assets/official-account-qr.png)

## License

MIT. 这是一个非常宽松的开源协议，适合 fork、改造、二次集成和内部使用。
