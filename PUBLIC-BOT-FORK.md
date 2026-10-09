# 公共机器人维护分支

分支：`codex/public-bot-server`

上游基准：`6087286c2ac79f4d10f810efec0deeef00b9abcf`

保留材料与背包绘图的错误缓存修复。依赖配套 gsuid_core 分支提供 gs_cache(skip_text=True)。/ys 路由和官方 QQ 接入端由 zzz-queue-obs 负责。

主项目：[zzz-queue-obs](https://github.com/Karl-Cao/zzz-queue-obs)。配置、用户数据库、Cookie、Stoken、机器人密钥、日志和下载的资源目录未作为本次修改提交。此分支归档已部署补丁；fork 本身不会自动切换线上服务，上游默认分支保留供同步。
