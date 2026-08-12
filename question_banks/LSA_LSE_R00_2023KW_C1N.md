---
schema_version: will-ai-question-bank/v1
source_pdf: LSA_LSE_R00_2023KW_C1N.pdf
source_sha256: fc60d3fccd1cd784233e95c31b708a2ac877e03874e892b9f9cfc617582f865c
source_pages: 34
question_bank_version: V1
product_scope: LSA/LSE
---

# LSA_LSE_R00_2023KW_C1N 题库与判定标准

## 1. Source Information

- Source PDF: `LSA_LSE_R00_2023KW_C1N.pdf`
- SHA-256: `fc60d3fccd1cd784233e95c31b708a2ac877e03874e892b9f9cfc617582f865c`
- Physical pages: 34
- Product: KOSMEK LSA/LSE 油压复动式侧向夹紧器
- Product printed pages: 947-958
- Included common-reference printed pages: 1725-1730
- Included control-valve printed pages: 1257-1262、1265-1272
- Included sales-reference physical pages: 33-34（无印刷页码）
- Source-evidence policy: PDF 页面图像是视觉事实的最终依据；抽取文本仅用于导航，不能作为来源真值。

## 2. Scope

### 2.1 Product and document scope

本题库覆盖 LSA 标准侧向夹紧器系列和 LSE 高能力侧向夹紧器系列，包括产品定位、
型号语法、规格、夹紧力与保持力关系、尺寸、安装、液压回路、速度调整、保养、
安全事项，以及本 PDF 收录的适用直装式控制阀。

商业质保和销售网络资料保留在来源清单中，但不纳入核心能力题。液压
安装、速度控制、操作、保养、符号和附属控制阀等通用事实必须采用限定到具体
页面的本地范围和正确的绑定类型，避免与 LSA/LSE 产品本地要求混淆。

### 2.2 Model Grammar

LSA 和 LSE 的印刷字段顺序为：

`<系列><主体尺寸><设计编号>-<配管方式><压板方向>`

| 字段 | 合法值 | 含义与约束 |
|---|---|---|
| 系列 | `LSA`、`LSE` | `LSA` 是标准侧向夹紧器系列；`LSE` 是带机械自锁机构的高能力侧向夹紧器系列。 |
| 主体尺寸 | `036` | 夹紧器本体夹紧部分外径等级为 φ36 mm。 |
| 设计编号 | `0` | 本 PDF 列出的产品版本/设计编号。 |
| 配管方式 | `C` | 板式配管型，附带 G 螺纹堵头，可安装另购的直装式速度控制阀。 |
| 压板方向 | `L`、`C`、`R` | 面向供油口观察时，压板方向分别为左、中央或右。 |

两个系列共用主体尺寸、设计编号、配管方式和方向字段语法，但使用限制和速度控制
规则并非全部相同。尤其是 LSE 必须使用进油节流型 BZL-A 速度控制阀。

合法示例：

- `LSA0360-CL`
- `LSA0360-CC`
- `LSA0360-CR`
- `LSE0360-CL`
- `LSE0360-CC`
- `LSE0360-CR`

非法示例及原因：

- `LSA0400-CR`：本 PDF 未列出 LSA 主体尺寸代码 `040`。
- `LSE0361-CR`：本 PDF 未列出设计编号 `1`。
- `LSA0360-SR`：本 PDF 未列出配管方式 `S`。
- `LSE0360-CB`：本 PDF 未列出压板方向 `B`。
- `LSA0360-RC`：配管方式与压板方向字段顺序错误。
- `LSE0360-CR-A`：BZL 控制方式不是 LSE 产品型号的后缀字段。

### 2.3 Source-first inventory and initial dispositions

`HIGH` 和 `MEDIUM` 项在对应问题及构建审计完成前均保持未完成状态。处置列仅标明
计划工作，不提前声明已覆盖。每一对物理页是同一印刷跨页的重复呈现；Inventory
只记录一次，不将重复页面视为新证据。

| Inventory ID | 物理页 / 印刷页 | 本地范围 | 证据类型 | 优先级 | 可测试对象 | 初始处置 |
|---|---|---|---|---|---|---|
| LSA-LSE-SI-001 | 1-2 / 947-948 | LSA 概述与特点 | TEXT + DRAWING | HIGH | 侧推定位、上方零干涉、安装尺寸通用性、2.8 kN 标称夹紧力及直装式速度控制阀 | WP2 `FACT`；保留图示本地限定 |
| LSA-LSE-SI-002 | 3-4 / 949-950 | LSA 型号、规格与夹紧力关系 | MODEL + TABLE + FORMULA + CHART | HIGH | 四字段语法、φ36 本体、行程/容量/压力/温度/流体/重量、`F = 0.394 x P`、压力-夹紧力表及不可使用范围后果 | 型号语法及 `LSA-LSE-Q-0001`；WP2 `TABLE`；WP3 `CALCULATION` / `CHART` |
| LSA-LSE-SI-003 | 5-6 / 951-952 | LSA 尺寸、设计、安装与速度控制 | DRAWING + TABLE + TEXT | HIGH | 油口、安装几何、禁止同时供压、焊接/干燥环境控制、M4 力矩、销轴操作和速度调整 | WP2 `TABLE`；WP3 `PROCEDURE` / `CAUTION`；重复尺寸保留为直接查询证据 |
| LSA-LSE-SI-004 | 7-8 / 953-954 | LSE 概述与高能力机构 | TEXT + DRAWING | HIGH | 侧推定位、相对 LSA 的 1.5 倍夹紧力、机械自锁、保持力作用及 BZL-A 要求 | WP2 `FACT`；WP3 `CAUTION`；机构图留待选择性视觉核验 |
| LSA-LSE-SI-005 | 9-10 / 955-956 | LSE 型号、规格及夹紧力/保持力关系 | MODEL + TABLE + FORMULA + CHART | HIGH | 共用四字段语法、行程/容量/压力限制、`F = 0.601 x P`、`Fk = 0.953 x P`、3.62 kN 保持力上限及反作用力注意事项 | 型号语法及 `LSA-LSE-Q-0001`；WP2 `TABLE`；WP3 `CALCULATION` / `CHART` / `CAUTION` |
| LSA-LSE-SI-006 | 11-12 / 957-958 | LSE 尺寸、设计、安装与速度控制 | DRAWING + TABLE + TEXT | HIGH | 方向变型、安装几何、禁止同时供压、M4 力矩、进油节流调整、排气、多夹紧器控制及带负荷释放 | WP2 `TABLE`；WP3 `PROCEDURE` / `CAUTION`；保留 LSE 本地回路例外 |
| LSA-LSE-SI-007 | 13-14 / 1725-1726 | 液压安装与速度控制回路通用事项 | TEXT + TABLE + STATE_DIAGRAM | HIGH | ISO-VG32 油品表、清洁、密封胶带、排气、紧固检查、单/复动回路规则及 LSE 例外 | WP3 `PROCEDURE` / `CAUTION`；限定页面的 `DOCUMENT_COMMON` |
| LSA-LSE-SI-008 | 15-16 / 1727-1728 | 操作、保养与质保通用事项 | TEXT + DRAWING | HIGH | 人员资格、隔离/零压/冷却、重启检查、禁止接触/改造、清洁、检查、存放及大修 | WP3 `CAUTION`；质保内容为 LOW 并排除；限定页面范围 |
| LSA-LSE-SI-009 | 17-18 / 1729-1730 | 通用符号参考 | TABLE | MEDIUM | 表面粗糙度及 O 形圈材质/硬度的新旧符号对应关系 | WP2 `TABLE`；限定页面的 `DOCUMENT_COMMON` |
| LSA-LSE-SI-010 | 19-20 / 1257-1258 | 直装式控制阀系列概述 | TEXT + DRAWING + TABLE | MEDIUM | BZL/BZT/BZX/JZG/BZS 的用途、直装关系和压力等级 | WP2 `FACT` / `TABLE`；附属产品范围 |
| LSA-LSE-SI-011 | 21-22 / 1259-1260 | BZL 低压速度控制阀型号与兼容性 | MODEL + TABLE + TEXT | HIGH | 螺纹/设计/控制方式语法、A/B 回路含义、压力/温度/力矩、兼容性、禁止重复使用及 LSA/LSE 对应关系 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION` |
| LSA-LSE-SI-012 | 23-24 / 1261-1262 | BZL 流量曲线、尺寸与注意事项 | CHART + DRAWING + TEXT | MEDIUM | 调整前后流量与圈数/压力损失关系、油口方向、低压排气和加工尺寸 | WP3 `CHART` / `CAUTION`；必须进行真实视觉读图 |
| LSA-LSE-SI-013 | 25-26 / 1265-1266 | BZX 排气阀 | MODEL + TABLE + DRAWING + TEXT | MEDIUM | 螺纹语法、35 MPa 限制、力矩、兼容性、堵头旋松限制及低压排气 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION`；附属范围 |
| LSA-LSE-SI-014 | 27-28 / 1267-1268 | 带排气功能的 JZG G 螺纹堵头 | MODEL + TABLE + DRAWING + TEXT | MEDIUM | 螺纹语法、35 MPa 限制、力矩/材质规则、兼容性及低压排气 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION`；附属范围 |
| LSA-LSE-SI-015 | 29-30 / 1269-1270 | BZS 直装式顺序阀型号与规格 | MODEL + TABLE + DRAWING + TEXT | HIGH | 螺纹/设计语法、压力范围、通路、力矩、兼容性、污染、压差、重复使用及流量控制 | WP2 `MODEL` / `TABLE`；WP3 `CAUTION` |
| LSA-LSE-SI-016 | 31-32 / 1271-1272 | BZS 尺寸、设定与动作顺序 | DRAWING + TABLE + CHART + PROCEDURE | HIGH | 调整范围、油口方向、压力设定、防转套力矩、动作顺序、多阀压差、空气及调试 | WP3 `PROCEDURE` / `CHART` / `CAUTION`；仅在布局关系不明确时选择性视觉核验 |
| LSA-LSE-SI-017 | 33-34 / 无印刷页码 | 销售地址与网络 | TEXT + DRAWING | NON-TEST | 联系方式和销售区域 | 排除；不属于耐久的 LSA/LSE 技术知识 |
| LSA-LSE-SI-018 | 1-32 / 全部收录印刷页 | 重复导航及成对跨页呈现 | TEXT | NON-TEST | 侧栏导航、章节标签、页面重复和交叉引用界面 | 作为导航/呈现重复排除；来源清单以本地技术内容为准 |

## 3. Question Statistics

- Total: 1
- MODEL: 1

## 4. Questions

## LSA-LSE-Q-0001

**Type: MODEL**

### Target

- Binding: MODEL_FAMILY
- Product: LSA/LSE 油压复动式侧向夹紧器
- Model / Scope: LSA0360-C□ 标准系列和 LSE0360-C□ 高能力系列

### Question

按 PDF 的型号字段顺序解读 `LSA0360-CL` 与 `LSE0360-CR`。说明两个前缀的
产品系列边界、`036`、末位 `0`、`C` 以及 `L`/`R` 的含义，并判断两个型号
是否合法。

### Standard Answer

`LSA` 表示标准侧向夹紧器系列；`LSE` 表示带机械自锁机构的高能力侧向夹紧器
系列。两个型号中的 `036` 都表示夹紧器本体夹紧部分外径为 φ36 mm，末位
`0` 是本 PDF 列出的设计编号，`C` 表示板式配管型并配有 G 螺纹堵头。面向
供油口观察时，`L` 表示压板向左，`R` 表示压板向右。因此 `LSA0360-CL` 和
`LSE0360-CR` 的字段顺序与取值均合法。

### Scoring Standard

- P1 [10]: 正确说明 `LSA` 是标准侧向夹紧器系列。
- P2 [15]: 正确说明 `LSE` 是带机械自锁机构的高能力侧向夹紧器系列。
- P3 [15]: 正确说明 `036` 表示夹紧器本体夹紧部分外径 φ36 mm。
- P4 [10]: 正确说明末位 `0` 是设计编号。
- P5 [15]: 正确说明 `C` 为配有 G 螺纹堵头的板式配管型。
- P6 [10]: 正确限定压板方向的观察视角为面向供油口。
- P7 [10]: 正确说明 `L` 为左、`R` 为右。
- P8 [15]: 正确判断两个示例型号的字段顺序和取值均合法。

### Accepted Variants

- `φ36 mm` 可写为 `Φ36 mm` 或 `直径 36 mm`。
- `板式配管型` 可写为 `板式连接型`。
- `机械自锁机构` 可写为 `机械式自锁机构`。

### Forbidden Errors

- 交换 LSA 与 LSE 的标准/高能力系列边界。
- 将 `036` 解释为行程、压力或夹紧力。
- 将末位 `0` 解释为方向或控制方式。
- 将 `C` 解释为压板中央方向。
- 不限定观察视角，或交换 `L` 与 `R`。
- 声称任一示例型号的字段顺序或取值非法。

### Tolerance

- 必须准确给出系列边界、φ36 mm 主体尺寸等级、设计编号 `0`、配管方式 `C` 和方向含义。

### Source

- PDF: LSA_LSE_R00_2023KW_C1N.pdf
- Physical page: 3-4, 7-10
- Printed page: 949-950, 953-956
- Section: LSA/LSE 特点 / 型号表示 / 规格
- Local scope path: LSA 标准侧向夹紧器与 LSE 高能力自锁侧向夹紧器；LSA0360-C□ / LSE0360-C□ 型号字段
- Evidence type: TEXT + MODEL + TABLE + DRAWING
- Evidence: LSA/LSE 特点页区分标准和高能力自锁系列；型号页给出“系列-036-0-C-方向”的顺序，将 036 定义为 φ36 mm 本体尺寸、0 定义为设计编号、C 定义为配有 G 螺纹堵头的板式配管，并以面向供油口的视角定义 L/C/R。
