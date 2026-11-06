# 更新记录

## v1.1.0 — 2026-11-06

素材更新。64 段，整体在竖向压缩 **7.5%**（脚底仍对齐 y=351，`body_box` / `head_box` 未改）。

- 分类：`idle` 6 / `random` 46 / `click` 8 / `move` 2 / `turn` 1 / `drag` 1（`events` 为空）
- 新增 `random/`：`吃Token`、`轻快记录`、`写代码`
- 补回 `random/`：`左右摇摆`、`平板`（与 `写代码` 内容相同、名字不同，按原样保留）
- 修正帧率元数据：`random/向前挥拳`（108fps → 24fps）、`click/点击回应-被按墙上`（60fps → 24fps），帧数不变
- 全部 64 段重新编码：640×360、24 fps、VP9、`alpha_mode=1`，`tools/check_pack.py` **64/64 通过**
- 体积 67.5 MB → **62.0 MB**（两条重编码叠加 + 像素面积减少）
- `preview/overview.png` 按 64 段重新生成

> 注：本版是在 v1.0.0 素材上连续两次重编码（5% + 2.5%）得到的，画质有轻微代际损失；
> 需要原始比例与首代画质请用 v1.0.0。

## v1.0.0 — 2026-11-04

首个版本。61 段动画，角色 ID `mesugaki`。

- 分类：`idle` 6 / `random` 43 / `click` 8 / `move` 2 / `turn` 1 / `drag` 1（`events` 为空）
- 全部 640×360、24 fps、VP9 Profile 0、`yuva420p`（alpha_mode=1）
- `manifest.json`：`body_box [220,16,420,351]`、`head_box [214,16,426,156]`
- `move_strides.json`：`漂浮踏步` stride 90、`左转奔跑` stride 220
- Windows 安装脚本 `install.ps1`：自动定位安装目录、备份旧角色、支持 `-Uninstall` 还原；
  检测到旧项目的 `bluewhale_tv` 时只提示、不自动删
- 素材自检脚本 `tools/check_pack.py`（`alpha_mode` 元数据匹配改为大小写不敏感：
  部分片段把这行写成 `ALPHA_MODE`）
- `preview/overview.png`：61 段总览图，每格取该段第 1.2 秒
- 全量自检（`ffmpeg` + `libvpx-vp9` 解码）：**61/61 通过** 640×360 / 24 fps / VP9 / alpha 平面可解

### 与 mesugaki-feiyu-pet 的差异

本项目是同一批动画的**完整版重新发布**，旧项目（47 段精选版，角色 ID `bluewhale_tv`）保持不动。

- 新增 14 段：`random/` 12 段（`可爱动作`、`戳屏幕`、`托腮思考`、`扭动挑衅`、`向前挥拳`、`暴躁跳跃`、`烦躁跺脚`、`短促跺脚`、`猫爪抓`、`拿出米饭`、`挤眉弄眼`、`吃光白米饭`）、
  `click/` 2 段（`点击回应-吃光白米饭`、`点击回应-电击抽搐`）
- 3 段在旧项目里是**改名后的同一素材**（字节相同）：
  `点击回应-吃白饭` → `random/喝水`、`点击回应-头发散乱` → `random/吹风`、`random/白米饭` → `random/啥也没有`
- `click/点击回应-被按墙上.webm` 与旧项目不是同一版剪辑（本版 601 KB / 旧版 1.03 MB）
