# 自动研究样例

## 触发样例

以下请求适合触发这个 skill：

- “帮我用多轮实验找出这个客服工作流最好的 prompt 策略。”
- “探索几种提升注册转化的方法，但不要一次改太多东西。”
- “研究三个 GTM 方向，逐步测试最强的方向，并保留完整日志。”
- “不要整体重写，迭代修复这个脆弱的 agent workflow。”
- “持续调查这个 onboarding flow 为什么表现差，并把过程记录下来。”

以下请求不适合触发：

- “总结一下这篇文章。”
- “修这个已知文件里的单个 bug。”
- “翻译这段话。”

## 重构样例

### 用户请求

“帮我想办法增长有效线索。”

### 用这个 skill 重构后

- Objective：提升有效线索数量
- Primary metric：每周有效线索数
- Guardrails：固定预算、禁止骚扰、未经批准不得外呼
- Action surface：落地页文案、报价角度、渠道假设
- Frozen surface：线索判定规则、统计窗口、品牌限制
- 首批轮次：先测 baseline，再测一个 offer angle，再测一个 CTA，再比较结果

### 用户请求

“持续优化这个 agent workflow，直到它足够稳定。”

### 用这个 skill 重构后

- Objective：提升流程稳定性
- Primary metric：固定场景下的成功率
- Guardrails：禁止生产副作用、运行时间受限
- Action surface：prompt、分支逻辑、校验步骤
- Frozen surface：评估场景和通过标准
- 首批轮次：先建立 baseline failure modes，再一次只测一个校验改动
