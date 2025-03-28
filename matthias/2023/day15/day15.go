package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

const (
	example = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
	day15   = "lqgpv=5,bvv=1,sls-,ttn=2,gvh=3,bgj-,zg-,sv-,fqz=7,ldb-,gvzx-,hh-,vbk=1,rnhrk=9,zvt-,zxk-,pvjz-,vx=7,rzq=1,snf-,zgk=9,pf=9,rmgxs=3,pjdrpt-,tlt-,vn-,tvr-,mjqhbk=6,shm-,klmlv=4,crh-,fjf=6,dfgz-,xhsp=2,bq=3,grdn=8,rz-,tbl=2,tv=1,rsvn=8,sj=6,nbds=5,xdj=7,hs-,bxk=5,dz-,tbtqj=3,kr-,lkqp=8,pf=9,nqj=4,sjxc-,nxk-,hls-,njgzf-,rtg=3,djrhq-,nm=4,zpm-,zqm=2,cp=9,bz-,tz=5,tx-,sjxc=9,tt-,qf=4,hf-,hkj=3,mjs=7,vsxfqp=6,tlf-,gfqclt=6,lnvkl=9,ptk-,cb-,lxc-,qx=9,ggq-,scq=4,kv=4,ctm=1,cs=8,fsxrqj-,ptbr-,prf=8,vx-,hjm=1,tkd-,ts=3,bnh=5,crg=4,ch-,xqbhnt=2,cx=3,fjf-,hkj-,fpx=6,phxjs-,tcmn-,hlcpzb-,nms-,ftk-,gfq=2,zxk=9,njgzf=5,pf-,pt-,jl=6,rr-,pgz-,jfsfp=3,kxf=3,mdqz-,rfl=6,xb-,bmjb-,gdld-,qtp=8,kbp-,klmlv=1,vzt=2,mm=8,gdld=5,cltgr-,gb=3,dp=1,sjxc-,zgk-,bvv-,nnpq-,qdsxq=5,bk-,nc-,tkd-,xrbt=4,lccj-,fdgp-,tvr-,rnhrk=9,jqc-,vdjz-,jqxl=4,nm=1,bnh=1,nm=8,pd-,fnd=1,njgzf=3,bmhf=3,hkj-,bk-,drsx=9,hh-,zqjprz-,vdsn-,ldb-,gpjnx-,xsg=8,sqq-,fl=8,nc-,gfq-,ft-,rt-,zqm=1,bpc-,prf-,pt=2,qglt=9,grs-,vkvm-,nsvgj-,tvr=2,fjf=5,vcv=9,mkk=6,ddpml-,rhd=1,jmb=8,lr=3,kvrfm-,gn=2,vd-,vcs=2,zxk-,tftg-,tbm-,mdqz-,vbk=3,hgb=9,nl=1,bhg=4,crg-,pvz-,ptkrnb-,bmmgsc-,tlt-,xxsfxb=8,bhg=1,bq-,hr-,cx-,mm=6,sjq-,dcp-,bfc=4,fbf=2,shqrb-,kbp=2,pvj=7,pjsvd-,bgd-,xsg-,bnjjz-,plfn-,hgh=1,vzt=3,sf=5,dfgz=4,czc=2,mjqhbk=3,sq-,pfvqp=9,ffzvk-,gpjnx=9,thp-,ktt-,vpxxc=4,crg=3,zqnp-,lqdd-,zqjprz=9,bj=8,cgln=9,fj-,qb-,kxf=4,cx=7,fr-,qmd=8,pt-,qfp=6,hm=3,fdz-,dzlvpk-,lh-,bzb=4,rmkb=7,tmtnb-,kmtk-,lxc=8,nrmt-,rsvn=7,zhzz-,jrl=1,gvzx-,slc=9,zgm=7,qzs-,nqj-,qgz-,nj-,szx=3,md-,ht-,rdm=8,vsxfqp=9,vkq=2,nm-,nzpbn=3,hjm=6,mkk-,mbrs-,mb=7,gnj-,xqbhnt-,kbg=5,qmd=5,pbpb-,nn=3,ptbr=1,xkd-,gd-,mr=1,hlcpzb-,qf=3,tcmn-,jsj-,lp=3,cpq=1,cc-,tms-,vdsn=6,rfl-,cs=9,lt-,pq-,cx-,dtfj=1,cg=9,lt-,qtl-,xdj-,cgtd=2,hsz=5,ds=6,vd=3,dl=1,vn=8,nkb=3,mdqz=5,vpj=3,kbg-,cvjr=8,bfbt-,flg=6,snt-,tdfx-,cgtd-,tdz=3,hq=5,pnrk=2,jclfth-,vzt=4,bmmgsc-,vbsrn-,hs=6,tqv-,nk-,dxts-,ch=6,cz-,qpm-,vmnt=4,fjrrm-,vkf=5,tbmr=1,hsz-,zxk=6,crg-,pln-,vpxxc=3,hjm-,lf-,tc-,fnd-,nnpq=9,vpcz=8,hf=1,fnd-,llr-,nqmq-,hjl-,zc=8,gn=1,zpm-,zcjx=4,kr-,lj=1,kvv=2,fbf=3,tmtnb-,nk-,czc=1,dtfj-,scq-,jxj-,bxk=8,jx=3,zftx-,njgzf=3,vmnt-,xmn-,dsj-,bfbt-,pjdrpt=1,bt-,czc-,pvz=5,fx-,zhzz-,mbrs=8,pmkqk-,jmtr-,xhsp-,dv-,fj=8,nxk-,vcv-,nj-,bmn-,gfgk=7,bb-,csmch-,dkvfsp-,scq=7,xxsfxb=7,mlzp=9,qqt-,rnhrk-,rnhrk=1,dnrx-,ctm-,zhv=9,grdn=9,vk-,sf=2,ds=8,tp-,dthz-,cx-,hlc-,tftg=4,vd-,cz=8,nk=6,nv-,tp-,tvlqfg=8,cgl-,ptkrnb=7,sx-,rfzs-,lccj-,ldb=3,lxc-,cgln-,gjx=7,tgzpz=4,zpm-,lq-,sxht-,gsp=8,fqz-,fj-,fjrrm=6,rmkb=5,hr-,nbds-,lfjj-,tkd-,hjl=9,gpjnx-,rr-,xtvm-,kvv-,hpp-,dgbzr=7,sdrk-,th-,hvvmc=8,nv-,prf=8,cf-,kv=4,bpc=5,vpj-,bxn-,flg=4,cs-,nms=4,gmpj-,snf-,pbpb-,vjjfgc=5,gtd-,cz-,dj=3,sv-,nqg-,rmkb-,zhv-,llr-,gdld=7,fpx-,sgh-,kfz-,mb-,dscl-,mhrvl=2,bmhf=7,bq-,dt=7,hm=1,sls-,rzl=7,mvd=3,qfh-,rc-,pq-,gfqclt=3,kk=8,ft=2,qglt=1,gfgk-,kfz-,kxf-,hfb-,xf=5,kmtk-,plfn=9,dgz-,zhpfgc=9,ksh=8,fhzj=8,rnhrk=6,xf=2,vfb=1,vmnt=8,lc=9,jz=9,cbttmk-,xg-,kzbcjm-,gjx=1,slc-,hjl-,tbmr=5,cltgr-,fhzj-,lf=6,dz-,ds-,pjdrpt-,lbjp=7,bzfvl=9,tbtqj=7,qpm=6,pbpb-,cnbf-,tt-,mkvv-,cxlhd-,htk-,xg-,jb=3,tdfx-,jmtr=4,tbtqj=1,sjxc-,bzfvl=7,gfgk=5,cp-,klmlv=8,fbm-,kp-,gh-,lvx=1,xc-,kr=2,cbttmk-,ktt-,kdb=3,jfsfp-,dfgz-,pbpb=7,rfl-,xg=3,pnrk-,flk-,dqz=8,thp-,kbg=9,df=8,vkvm-,kxf-,mb=5,pbpb-,sxht-,vnqqfc-,hnz=4,pqrg-,kzbcjm-,tq=7,bb=9,xc-,xkd=8,xmn-,cgln=8,vdsn=3,bvv=8,dmmk-,shf=8,pfvqp=5,qd=4,zftx-,rfl-,tkd-,cpn=2,ktt-,nkt-,nnpq-,mkk=7,dmmk=3,nh-,thp=2,rr=2,br-,zt-,lbv=3,dl-,lj=7,rfzs=3,vft=8,bt=9,kdm=3,ptk=1,dqz-,hl=9,xt=9,qx-,fjf=2,nkp=3,ksh=5,nl=4,gnj-,rr=9,pkzff-,xp=8,djrhq=8,njgzf-,np-,bk=5,sxht=9,gvh=5,bsflq=1,fbm=8,ch-,zvt=2,fx=2,cg-,pjdrpt=8,np=4,gh=5,mjs-,dthz=1,jxj-,rdm=7,cf-,rf-,mkd=3,fp=1,sls-,nl-,rzl-,rpmz-,vpxxc-,cx-,lkqp=9,th=4,kg-,cx=6,hr=9,cvfr=7,lnvkl=2,qpm-,np=1,sv-,hnm=7,bmhf-,cq=1,qf-,hmfc=6,nmh=9,qzs=9,tcmn=7,nrmt-,bfdd=8,mr-,grk-,fjf=8,jrl=1,gfqclt=7,llr-,rbs=1,br=3,ts-,gvzx-,snf-,hm-,zgb=9,lkqp=3,tx-,tcmn-,ggq=7,vqzj=3,hlcpzb=3,dkn=6,rtg=2,cgl=4,hs-,zqjprz=6,dxts-,zsq-,lrc=6,fl=7,qgz-,nv=1,jmtr-,vmnt=3,ldb=8,gg-,mjqhbk=3,mdx-,hfb-,nms-,ptkrnb-,grdn=3,mlzp-,vxf-,sqq-,ptkrnb=4,qfh=5,ldc=1,tdz=5,vqzj-,dnrx=9,bnjjz=1,hls=3,cxlhd=1,kxf-,nq-,zg=5,vkf=2,gvh=5,gsp-,cs-,qqt-,nj-,hgb-,cbttmk=2,sgh=9,jqxl-,kxs=1,jx=9,pt-,rpmz-,grk-,xsg=6,dj=7,pjr=2,kvrfm=5,plm-,lccj-,zcjx=2,tbmr=1,slc=6,pb-,nm-,ffzvk=1,tc-,rzh-,sj=3,qhs-,kdb=1,lt-,hls-,cx=9,qcc=1,nc-,rdfr=1,tvlqfg-,cz=2,bpc=7,bmn=4,zj=5,cgln-,mvd-,kp=4,gt=1,djrhq=8,lc-,tz=3,vpxxc=3,dmmk=1,ldb=8,plfn=5,ppzh-,xdg-,drsx=1,hsmkv-,vpj=7,hmfc=1,fpm=3,qzs=9,pv-,zr-,fpm-,cpq=7,kdm-,ttn=5,dmq=3,qf=6,fmqbk-,zgm=5,gtd-,nh-,szx-,rp-,vmnt-,llr=7,vdsn=5,qglt-,bvv=9,ps-,hgh-,hm-,bxk-,bgd=9,zrbc-,lr=1,kjls=8,jfd=8,ksh=1,vft=2,vdsn-,lkqp-,tdz-,ms-,cb-,rc-,gb=5,dt=1,hgh=5,sq=5,grdn-,llr-,lp=9,rt-,qb-,rc=9,nq=4,tqv=2,zf=9,sdrk-,cpn-,nbc-,zh=1,sls-,fdgp=9,xxsfxb-,vpj-,hs=2,bmn-,ch-,zqm-,cpq=9,tp-,qtp-,lf-,fgf-,nk=7,gg=9,qpm-,hb-,ptkrnb=3,lf=1,bmjb=5,rnhrk-,dp-,rt=9,xq-,tftg=9,dsj=3,jb=8,ptk-,fjrrm-,fpx-,ldb-,qb-,ptk=1,zhzz=9,gkcr=6,grs=4,dlt-,tx=9,mn=7,vbsrn-,xb=7,bmmgsc-,qzs=5,pq=4,vx-,zqm-,cs=4,sjcf=6,dvq-,sp=5,gg=3,rzh=2,qtl-,vmnt=3,hjm-,hr-,cp=4,jl-,pjr=3,zpm=2,pkzff=1,qmd=6,zpm=6,md=2,tdf=4,tcmn=3,vdpj=6,vpcz-,kvv-,hl-,bhg-,sjxc-,lc=1,hsz=2,flg-,shm-,tmtnb-,xkd=1,nk=8,plm-,vdpj-,pbpb-,tz=8,lxc-,grdn=1,qr=3,npcxkn-,zh=8,tv=9,ptk-,rmkb=1,xdj=9,snf-,fl=1,lj-,kk=5,gz=5,tgzpz=8,fdgp-,mdqz-,crg-,md-,pbpb=1,bhg=9,grk=4,pln=6,vsxfqp=4,cltgr-,cgln-,gfq-,pjr=1,bmmgsc-,mh-,dmtdl=6,rz=9,jmtr=6,czc-,cgln=5,dk-,mm=5,cvfr=4,dlt-,mxc=5,sqq=8,bhg=9,mkd-,lzn-,lf-,kdb=3,fdtl-,vb-,njgzf=9,vk=1,nbc=8,lnvkl=1,dl-,lzn-,cvfr-,flg=1,nsvgj=6,sjq=1,vdsn-,nst=7,ppzh-,mv-,tkx-,rf-,vx-,zxvqk=7,tcmn-,mxc=5,ffzvk=3,cl-,zqbr-,fnd=2,pbpb=6,dsj=4,pl=1,hs-,pkz-,qkfp-,plfn=5,lrc-,gvh-,thm=6,rzq-,nzc=1,dfgz-,nkb=8,zqnp=1,sjq-,bk-,fjmc=4,gtd=9,ppzh-,vx=2,dv-,lq-,rdm=8,bhg-,lq-,xqbhnt-,slc=9,gdld-,dlt=3,vss=2,qtl=8,rf-,rkv-,zt-,fmqbk-,tvttkp-,thcs-,vdpj-,bnh=5,gxpr-,nl=5,vxf=3,gt=6,nm-,tvr=6,qf-,bfbt-,xq-,snt-,pjr=6,hnm-,mvd=3,lzn=3,dh=7,llr=1,kg=8,bzb=8,pgz=4,cxlhd=3,thcs=9,cvfr-,xb=6,dl-,tmtnb-,kk-,gmpj-,bk-,tqv-,zjm=6,vk=1,kbg-,hb=4,hsz=1,tvr=9,zvt-,ptbr=3,pjl=7,dthz=2,vd-,bj=6,cfb=7,vcs-,dj-,zsq=5,cv-,cgtd=1,nqmq-,prs-,vnqqfc=7,tvlqfg-,dj-,dscl=5,xd=6,hmfc=2,pf=9,hjm=6,mcq-,vpj=5,mkvv=9,rfzs-,dz=2,nmh-,nh=3,pv-,jl-,ptbr=6,fsc=2,sjxc=6,rkv=9,dthz-,zqjprz=8,zqm-,ps-,xf-,kkgt-,fdz-,bb-,dp=3,cp-,pvsb-,bfc=6,bfdd=6,fjf=9,dz-,tdz=2,dl-,xf=5,zlms-,fsxrqj=5,jfsfp=4,kbp=9,bxk=9,thcs=9,nc-,sxht=1,zh=9,jsj=6,jx-,md-,vzt=9,nk=1,kdm=3,fdtl-,pjsvd=6,nkt-,fsc-,vzt=2,vbk-,bhg-,bt=1,ms=4,zqm-,cl=9,hsz=8,cb-,qx=8,dfgz=4,zg-,xg=4,pd=3,zlms=2,ptbr-,pvz-,lj=2,rc-,qfh=8,sh-,jfsfp=5,kbp-,np-,kjls-,cq-,bsflq-,hjm-,bmmgsc-,njgzf-,prs-,cpq-,gpjnx-,pb=8,cbsmlt=4,dsj=1,vkvm=9,prs=1,crh=5,dgbzr-,hl-,kr-,hfb-,gkcr=7,sh-,sljtvf=4,tqv-,mkvv-,pbpb=3,vd=7,zcjx=9,pkz=9,dcp-,mkvv=8,tdz-,xtvm=2,rnhrk-,vqzj-,sq=8,vqzj=6,pjr-,hl=2,rr-,grdn-,hm=6,lccj=1,cx-,dthz-,gb-,cf=1,bfbt=5,qb=8,pnrk=4,zgm=5,nmh=4,qqt=5,lqgpv=5,btncfk-,zhv-,grk=2,kxf-,vz-,dp=2,qfp=3,kmlft=8,gz=3,gz-,jrl-,zlms-,pjr=9,dlt=5,mjqhbk=1,fpx=6,ptbr-,slc=6,gmpj=1,sljtvf-,zpm=8,vcs=4,tmtnb-,bq=1,ctm=5,zsq-,pkc=8,tp-,kmtk=3,ggq=4,nst-,vfb=3,zhzz-,vz=9,kmtk=7,fjmc-,ttn-,xdk-,lzn=5,qd=8,lrc=9,rsvn=7,dz-,sdm-,zr-,szx=3,nkp=7,dmtdl-,hgb-,hfb-,xt=5,mlzp-,pfvqp=4,nqj=1,fj-,prs=2,ddpml=8,zgk-,fx=9,vpcz=1,bnh-,flg-,rz=4,vd-,ldb=9,tbm-,zrbc-,kp-,gn=6,dbblf-,kfz=1,fgf=6,kdb-,jz=3,kkgt=1,nrmt=3,vcs-,df=2,bxk=5,cx-,lrc-,bnh=7,vzt-,ddpml-,xxsfxb-,pkz-,rr=3,lfjj-,lkqp-,dcp-,nmh=2,qpm-,tdz-,jz=8,vpcz-,nl-,xxsfxb=4,gd=9,bmn=4,ftk=1,rmkb=8,vq-,dscl=3,lr-,ldc-,dthz-,tq=5,kp=9,cf-,vxf-,ptkrnb=9,sdrk=4,bmjb-,zg-,dj=9,lqgpv-,vmnt-,qpm=5,bfdd=6,qfh-,fjf-,dgz=5,zr=8,rmgxs-,rc=3,xdk-,lqgpv=9,kxf-,hv-,md=7,lj=3,nzpbn=3,gpttz-,vtmxq-,hd-,bmmgsc=3,zxk-,hp-,cvjr-,fp=1,hsz=4,mvd=6,thm-,xp-,xsg=9,sgh=5,lj-,lfzf=9,dkz-,ch=1,zhv=7,jsj=9,vpxxc-,qzs=6,jmtr-,kvrfm-,rkv-,sv=6,zhpfgc-,zhv=9,qpm-,kvv=1,dqz=1,lxc=8,qcc=5,vft-,thm=2,hkj-,jfd-,bhg-,dfv-,tx=4,xhsp-,ddpml=6,vsxfqp-,thcs=1,phxjs-,gz-,xqbhnt=8,cpq-,phxjs=7,nkb=3,cf-,kr-,jfd=2,nzc-,vq=8,ch-,hf=5,bmmgsc-,rzl=7,sf-,fhzj=4,nbds-,cx=7,zr=6,pq-,bfdd-,fmqbk-,hl=6,skpk=9,bxk=2,rzq=7,qq-,pgz=9,rdfr=8,rrnz-,qr=3,vkvm=5,gfqclt-,tgzpz-,cs=1,snf-,mm=1,bvv=5,gs=9,fsc-,np=4,cbttmk-,kxf-,ft=6,nkb-,mkvv-,lccj=2,lr-,shm-,kh=4,qcc-,zqbr-,ssz=1,fdtl-,sq-,cpq=2,tbtqj=1,pvz=1,xc=4,bmjb-,lkqp=5,rzl=9,hl=3,cg-,fjrrm=8,xsg-,ffzvk-,qhs=7,jfsfp=7,hgh=8,bsflq-,vsmvd-,tnkx-,fr=5,rmkb=7,rt=9,cl-,ddpml-,bk-,prs=7,kg=1,vcs-,zrbc-,gz=5,hglng-,nn=3,sf-,vbk=5,ksh-,kdb-,zxk-,xkd=6,vtmxq=8,sjxc=1,cbttmk-,gkcr=7,bpc=4,tvttkp-,fjmc-,kg-,nh-,crg-,zhzz-,hmfc-,pjdrpt=3,ldb-,dlt-,xdj=2,mjqhbk-,rr=6,qd-,tvttkp=7,gd-,kvrfm-,fpm-,dh-,sdm=7,zg-,rsg=8,xqbhnt-,bj=7,zpm-,dkz=5,crh-,slc-,cg=7,pbpb=6,dnrx=1,sjq=3,fsxrqj-,znbpk-,jsj=1,hkj=5,hkj=1,lbjp-,gs=4,mn-,tkd=6,zt=8,dkz-,mkk-,tpnf-,rr-,vbsrn=5,qcc-,prs-,mjs=4,fbf-,rr-,qzs-,jfd=6,sxht=9,rt-,qpm-,rmlm=4,vsxfqp=9,szx=7,zxk=9,hf-,mdqz=8,kk-,qdsxq-,br-,thp-,nms-,zhpfgc=1,lq=3,vq=5,kbg-,pgz-,mjqhbk-,xtvm=4,hlc=4,mv-,nl=1,dtfj-,mvd=3,jqxl-,th=1,qcc=6,pjdrpt=5,qgz-,dp=5,rp=4,xvz-,tgzpz=1,qcc=1,cgtd=5,hmfc-,qgz=1,lfzf=7,dsj-,jsj=8,vnqqfc-,bj-,bz-,gfq-,pkzff=8,xkd-,sdm-,kmlft-,dlt=7,qr-,hkj-,tlf=9,sv-,vpj-,snf-,cvfr-,qd-,pkc-,kv-,nsvgj-,qd-,kfz-,rzl=6,vdsn=8,tlf=4,kp=9,vcs-,nkb=5,dthz=4,cfb-,bnh=9,pbpb-,qcc=7,dj-,zgk=1,np-,rpmz=1,ffsn-,nkb=2,lr=5,lbv-,qcc=3,rpmz=3,sls=1,jmb=3,rzl=7,rfs=8,nqmq=2,bsflq-,vpcz=2,nm-,lbjp-,pvz-,lf=3,bq-,jx=6,qhs=8,fsc-,vpj=6,gjx-,bmhf=6,gs-,nrmt-,dxts=3,cg=3,dkn-,pln-,rzq-,xf-,dfv-,ffzvk=9,ptkrnb=5,jmtr=2,gnj-,zhv=4,sdrk-,fdgp=1,tdf=6,sdm=9,plfn-,bfbt-,fp=1,nv=7,cmb-,rsg-,bgd-,kxf=1,pq-,fqz-,sdrk-,lq=3,vmnt-,nms-,cx-,fjrrm-,hls=3,qmd-,hlcpzb-,bsflq=8,bpc=8,nbc=4,fjmc-,fjf=7,vq-,lkqp-,xhsp=3,vdsn=2,vpcz=3,zgm-,kjls=2,kbp-,ppzh-,qgz-,xhsp=7,lvx-,qcc=5,xhsp=6,nl-,js=2,hnm-,qqt-,znbpk-,fdtl-,hr=4,snt-,xg=6,ffsn-,fl-,dtfj-,tp-,njz=1,scq=4,prs=6,hpp-,mlzp-,fp-,ht-,vdjz=4,sh=5,fbf-,lxc-,dz-,qhs=6,sdrk-,tt-,lkqp=3,qzs=2,fjf-,hmfc-,bfbt=5,dgbzr=9,pjsvd=6,tp=9,qhs-,lbjp=8,zvt-,bnl-,cpn=1,qdsxq=5,vz=1,gt-,slc-,bmjb-,pgz-,nh=1,ptbr-,tqv-,md=3,zqjprz=2,jx=2,rnhrk=4,cpn=9,ftk-,zh-,jmtr-,mh-,mn-,dzlvpk=4,pfvqp-,rfl-,tdjzd-,fl-,md-,thcs=5,kk=1,qmd-,cb=6,bj=9,xdg=7,gmpj=6,nkb=4,xb=3,vsmvd=5,xc=5,xkd=1,kvv-,cltgr-,mcq-,hvvmc-,jl=6,mjs-,vdpj=3,gkcr-,rfzs-,vcs-,zhzz=8,kk=4,nj-,dtfj=8,mm-,pq=6,dbblf-,dqz=6,ftk-,qgz-,jqc=6,lkqp=5,fl-,jrl-,dcp=5,hq=6,cbsmlt=8,dzlvpk=8,vsmvd=1,thp-,lj=6,nq=3,nkp-,mdx-,sx=4,vb=8,tx=7,xtvm-,kjls-,zgk-,rkv=3,pvsb=5,tdfx=6,rp=4,zftx-,pv=3,cz=2,nq-,rdm=8,tkx=8,gkcr-,bb-,vpcz-,tv-,df-,mvd=2,rsvn-,ctm=4,rr=4,snt=4,xxsfxb=9,bz-,qf=9,kk-,lr-,jx-,kzbcjm-,pkc-,pvsb-,pjl-,pkz-,cp-,drsx-,rkv=2,zh=6,bmmv=5,gvzx-,xqbhnt-,cq=7,njz=4,pjl-,zr-,sx=6,dqz-,xc-,hjm=8,tpnf=7,mkvv-,jz-,rfl-,nzpbn-,fdz-,dqz-,zqjprz=1,mjqhbk-,fdgp-,dk=7,jmb=4,nqg=4,vft-,ch-,pvjz=7,bfbt=4,hgh-,nrmt-,cxlhd=2,fdtl=7,qgzmb-,xt-,hv=7,shf=6,dp-,rrnz-,nxk=1,pkc=5,nzc=1,zxk=6,ldb-,nzpbn=1,tbtqj-,kjls-,kxf-,hf=2,vqzj-,rp-,cm=3,rz=8,zjm-,nbds-,pgz-,lr-,prf=6,mdqz-,mh=2,zhpfgc-,prf=7,bj-,gdld-,mkk=4,bgd-,dzlvpk=2,kk=3,sv=2,cf-,nsvgj-,hpp=8,sq=2,nqg=1,vqzj=7,fnd=8,qgz=6,skpk-,vsmvd-,dfgz-,mlzp=4,ppzh-,ptkrnb=3,jfd-,nl-,vbk=2,rtg-,gvzx=8,lzn-,bnjjz-,dp-,dscl=3,mbrs=4,tms=7,jrl=4,kzbcjm=5,hls=4,gd-,vdsn-,dfv-,ttn=6,bsflq=1,lt=8,cbttmk-,ptk=5,tdz-,xp-,kvrfm=6,lbv-,dxts=6,zpm=3,hv-,zhv-,pmkqk-,dt=1,tv-,qcc-,gjx-,qmd-,tvttkp-,jl=6,pqrg=5,rsg-,nbc-,gbvf-,cm-,fl-,tvlqfg-,kjls-,rnhrk=1,hjm-,cpn=1,tdjzd-,dthz-,dgbzr-,ptbr=9,gmpj=7,tlf=4,thp-,mb-,gpjnx-,scq-,vsmvd=3,ckss-,tlf-,lzn-,hr=2,xkd-,vk-,rpmz-,rzh-,rtg-,lkqp-,prf=6,dkvfsp-,dgz-,hb=3,lbv=9,fsxrqj=2,nrmt=6,plm-,nzpbn=5,ts-,zf=8,gs=1,lc-,tv=5,dcp-,shf=4,lfjj=5,sjcf-,gfqclt-,pjsvd-,nk=9,rsg-,tftg-,zgb-,vd=2,kh=2,bfdd-,pqrg=1,xg=1,fjmc-,ksh-,dmq-,ft=5,hnm=8,rdfr-,pv=7,sf-,gtd=9,dthz=5,zhzz-,pbpb=7,njz=2,shm=3,pbpb=6,rzq=9,gnj=8,rrnz-,csmch-,nqmq=9,tnkx-,ppzh=1,rsg-,rmlm-,sdrk-,sjq=5,gmpj-,hglng=2,kmlft=7,nm-,hgh-,pkzff=2,vdsn=8,qhs-,vsxfqp-,xd-,fjrrm=2,mkvv=5,bmjb-,tvttkp-,lzn=4,xdg-,hsmkv=7,cmb-,fp=6,sdm=9,ht=9,jx-,vsxfqp=3,dt=1,lvx=6,klmlv=5,cg=4,tdjzd-,szx=3,sv=1,qglt-,vdsn=4,vn-,pt-,zqnp-,nbc=4,zvt-,grdn-,gs=8,vfb-,znbpk-,plfn-,xp=3,vpxxc=8,bmmv-,flg-,zrbc-,nbds-,ssz-,xf=4,lr-,rhd-,cpn=1,kbp=7,bq=7,rmkb-,sjcf-,pf=7,mqjk=5,dl-,kg=2,gfq-,jp=5,jrl=2,fjmc-,lqgpv-,hmfc=2,thp-,qfh=9,hvvmc=1,htk=2,gz-,gbvf-,bnjjz-,ts=2,jrl-,tv-,cs-,tt-,dkvfsp=9,mlzp=2,tmtnb=1,gbvf=2,lq-,zgk-,ldb=8,gt=2,zhzz=9,cbttmk=7,klmlv=6,dxts=9,thm-,xg-,qr=5,bnjjz-,dkvfsp-,ks=5,hls=4,klmlv=9,nbc=8,pjl-,ktt=6,gpjnx=9,cs=4,kvrfm-,njgzf=9,bmjb-,kjls=8,tp=5,ms=6,cx=4,gvzx=4,nms-,mr=7,hvvmc-,thp-,sqq-,dthz-,djrhq-,ptkrnb=4,gnj-,bnh=6,hpp-,nj-,cs=7,qb-,vz=8,tms=4,bsflq=5,tdfx=5,grk=7,tmtnb=1,fmqbk=3,tqv=8,dnrx=7,gt=6,bgj=9,nrmt-,kbg=5,cv-,zsq=8,nxk=8,csmch-,fl-,njgzf-,dbblf=6,vq=9,cc-,hq-,sjcf=7,cpq=3,zc=6,xvz=4,dqz-,fdgp=2,sjcf=6,ts=3,gfq=8,mxc=3,kmlft-,gnj-,sj=8,rdfr-,dfv=2,lh=2,hp-,bxn-,nnpq=5,hf=7,qgzmb-,tt=9,rdm=1,bfbt=7,cbsmlt=5,lkqp-,tb-,lbv=3,tc-,pbpb=7,hpp=8,zt-,xvz-,rzh-,pfvqp-,dj=8,gsp-,hglng=1,ffsn-,kdm=4,fbf-,gbvf-,bfc-,sdm-,pkz=5,hgb-,tdjzd-,pkz=3,fnd-,nq=3,gvzx=4,hlcpzb-,lrc=1,ttn=6,gnj-,ds=1,tms=9,gdld=2,znbpk-,zsq=1,rmlm-,rpmz-,fjmc=4,jclfth-,dcp=9,ddpml-,vkf=6,njz=2,hp=1,hs-,jp=9,npcxkn=4,fx=7,lzn=1,rf-,cbttmk=9,tt-,jb=9,tpnf=4,vpxxc-,hh=3,gnj=5,dcp-,qk=9,bnh=3,bk=5,nxk=6,fnd=4,zjm-,tc-,tcmn-,npcxkn=1,xdg=1,nj=9,rzl=9,dkz=8,hgb-,shqrb=4,fqz-,zxvqk-,xqbhnt-,gsp-,pvsb=7,md=7,hgb-,rtg=3,gbvf=9,rkv=5,rnhrk-,plm-,sv-,rf=2,hfb=2,fjmc-,hnm=5,zgb-,njz=4,cfb=5,hlc=4,jrl-,cs=3,zjm-,zqm=9,pjr=1,bzb=4,ggq=8,cz-,sljtvf-,vkq-,pjdrpt-,fpm=3,grk=6,dkz=3,lqdd=1,hgb=2,dvq=3,cltgr-,xf=3,lkqp=6,szx=7,pkzff-,rf-,dkz-,tkd-,vmnt=5,dmq=3,zjm-,nkt=7,tv-,zr=1,zc=7,lvx-,kxs-,pq=3,lc=3,sjxc=2,mlzp-,mdqz=2,mhrvl-,ms-,gfqclt=4,kv-,bpc-,gbvf-,js=9,xdk=6,hmfc=4,szx=4,mb-,gn=8,prf=4,bxk=5,dmmk=6,cg=5,bfc-,fjmc-,gvzx=6,tnkx=9,qq-,fbf=2,kzbcjm-,dkvfsp-,fnd-,vz=5,xsg=4,fpx-,jmtr=2,cl-,cx=1,qfp-,dgz=2,xp=9,hd-,lqgpv-,hjm-,th-,mbrs-,pjr=5,nn-,nj-,nst=6,rhd=2,fdz=6,ftk=6,qd-,hglng-,tpnf=7,xdk=1,sj=5,kg-,mh=8,ggq=4,tlf-,xp-,bxn-,xrbt-,qcc=5,plm=4,mhrvl-,dv-,hvvmc-,fpx-,lbv=4,ksh=6,zxk-,zftx=5,dj=5,mb-,dh=5,xp=5,xrbt=8,hkj=6,ks-,rhd-,kr=6,ssz=5,jsj-,jz=2,thcs-,zc=3,rzq=8,tlf=2,pl=7,mcq-,lkqp-,tt-,mlzp-,bfdd-,dq-,plfn=4,szx=6,tz-,df-,jrl=2,pkz-,zhpfgc-,mvd=3,sls=5,nbds=6,hb=5,bmhf-,zhzz-,htk=6,rkv-,tcmn-,sdm-,prs=4,mlzp-,sgh-,rrnz=9,nh-,gpjnx=3,qdsxq=6,ttn-,qglt-,cvjr=3,nms-,gjx-,zjm-,rsg-,fdz-,tq=5,kbp-,lj-,tbtqj=9,kdb=7,vbsrn-,kp=1,zhpfgc=6,jrl-,pbpb=7,rzq=8,lbv-,ds=6,tq-,rmlm=7,cx-,pf-,pq=8,hd-,ds=6,ptbr=9,bxn=7,rt-,flg-,hpp=7,slc=5,dbblf=6,tv=1,hv-,bxk=6,pkc=3,qfp-,mdqz-,nzc-,lfjj-,cl-,lbjp-,pjsvd=5,lqdd-,dmtdl-,nc-,vtmxq=8,jclfth=9,hglng=9,ft-,vtmxq=3,rtg-,plm-,fjmc-,lccj=5,zhzz-,fmqbk-,bt=8,cpq-,lxc=3,fdgp=2,snt-,tlt=5,kk-,pf-,nms-,dkz=8,phxjs=1,nqj=9,cmb=3,jx-,bgd-,gbvf=3,xtvm=9,xf-,bsflq-,vx=4,znbpk-,ks-,lf=3,dqz=9,sx-,ldb-,vdsn=9,gxpr-,vkf=5,tdf-,hm=4,bzb=7,gddbz=1,kk-,rsvn=5,dq=3,bz-,gddbz=4,snt-,tdjzd-,hsz-,hkj-,zxk=1,pqrg-,nrmt-,lfjj-,lzn=3,tftg-,xb=1,vpxxc=2,ks-,xg-,htk=3,rdfr=3,rr=1,pvsb=8,sjxc-,mbrs=7,sjxc=4,rzl-,gz=2,zc-,cl-,pbpb-,gdld-,zh=2,hlc-,vkf=4,dfv=4,hnm-,klmlv-,kv-,tz=2,vsmvd-,nv-,czc=3,vft-,pmkqk-,rz-,qgz=7,gpjnx=9,jmb-,lbjp=8,sp-,cpn=8,shf-,rmkb=4,plm-,dcp-,cq=1,pq-,ps-,jqxl=5,cgtd=1,hsmkv=6,md-,jclfth=5,cnbf=7,xvz=3,pkz=1,qfp=4,zpm=6,kg-,bhg-,xdj-,dtfj=5,hm-,gvh=9,ldc=6,vtmxq-,fsxrqj=2,pfvqp-,fp=3,mhrvl-,mh-,hs-,npcxkn=6,plm-,kxs=3,dvq-,lqdd-,flk-,js-,vkf-,vtmxq-,zgm=5,tms=6,bfc-,qpm-,pf=4,ts-,mdx-,kvrfm-,tlf-,hpp-,kv-,vkvm=7,pln-,dgz-,mv=4,vpxxc-,grk=2,mhrvl-,dt=5,ht=7,dq-,hh-,jmtr-,cbttmk=1,xc-,ts-,prf=4,zhzz=8,hmfc=6,lf-,dbblf-,czc=2,sp=8,cvjr=1,dkn-,kvv=8,nm=7,rzh=2,znbpk-,th=5,tlf=4,bk-,vpj-,ps-,ftk-,cgtd=3,npcxkn-,sls=2,scq-,nmh-,gmpj-,pbpb-,gkcr=5,lvx-,kxf=8,hmfc-,kbp-,nst=8,jrl-,qf=6,lxc-,fdz-,ffsn=9,gfgk-,nkb=2,djrhq=3,dtfj-,rfs-,nnpq-,hm-,thp-,ptkrnb=1,kk-,fjmc=3,hlcpzb-,ch=1,cc=4,bz-,tv-,hr-,vdsn=3,ctm=2,pvj-,shqrb-,vsmvd-,jqxl=2,vss-,pkc-,fjmc-,fdgp-,nqmq=7,lqdd=6,tnkx=1,shf=9,vzt-,rzh=2,ts-,qb-,tms=2,tvlqfg-,zqm-,cmb-,dgbzr-,qkfp=4,fbm-,zqm-,mhrvl-,ht-,bzfvl-,vbsrn=2,xvz=9,crh-,btncfk=7,dl-,dthz-,lfzf=8,bxn-,pkz-,vjjfgc-,shqrb=2,xrbt-,bk-,gkcr=5,vss=7,mm-,dthz=8,kxs-,qf-,dmq=7,gjx=7,gbvf=3,hls-,gg-,zr-,zgk-,kbg=8,kxs=8,znbpk-,cg=6,dz-,dmtdl-,xhsp-,rhd-,lkqp=4,cf=2,fl-,czc-,bhg-,fx=3,bxk=5,zqjprz-,gs-,cfb=1,hr-,sgh=8,rt=5,xdj-,gfqclt-,cq=7,tbm=1,rzl=1,bgj=6,pkzff-,hlc-,bz-,xdg=3,lbjp-,shf=7,gjx-,pmkqk=2,tdfx=3,klmlv-,vsmvd=4,cf-,ffzvk-,xrbt-,pmkqk=7,xtvm=2,zhpfgc=3,hjl=5,kbp=5,drsx=8,vpcz-,rpmz=1,tms=4,lh=2,rnhrk-,cq-,lxc-,fr=6,dkn=1,mjs-,nq-,sqq=8,jqxl=2,gs=9,cvjr-,qtp=2,cgtd-,cq=2,ht=6,kr=7,qfh=1,bfdd=4,mr-,vbk=4,bmmgsc=7,pjr=3,qqt=2,tbl-,gmpj-,qfp=7,cm-,bq=2,bfdd-,pvjz-,kr=7,dkz-,hkj-,mhrvl=9,rfl-,kbg=9,zxk-,lq=4,xc=7,fjf=9,rfl=8,dxts-,mvd-,xc=6,fdtl=3,kxf-,rrnz-,dxts=3,rdm-,pnrk=6,thp=6,mr=6,tbl-,gnj-,df-,pt-,nzpbn-,zf=9,pkc-,pkzff=7,nkt-,mjs=3,rpmz=1,pvj-,czc-,rbs-,sgh-,dv=2,zt=3,qpm-,bnh=3,tbl-,nrmt=8,dsj=7,gvzx-,fjrrm=6,dbblf-,hd=1,qd-,htk=9,ldc=3,tx=3,nmh=2,lrc-,pln-,dzlvpk=1,qglt-,qmd-,vfb=2,xg-,nms=1,fbf-,prs=8,lbjp=9,nj=1,hlcpzb=7,bpc=1,vmnt-,sf-,gn-,cp-,hjl=7,lh=1,lf=7,xq=9,nzpbn=6,kv=4,sq-,mkd=3,fbf=4,cvfr=6,ks-,dcp=4,mhrvl-,slc-,mm-,pgz-,rsg=5,dk=8,thp-,vzt=2,hsz-,zf-,nj=6,sv-,pvjz-,ptkrnb-,lbv-,qfh-,tbl-,bnh-,hp=8,ctm-,rfs-,ts-,tkd-,fjrrm-,vbsrn=8,lbjp=7,qfp=3,nst-,dbblf=7,fhzj=7,xq=3,fdgp-,hls=9,cz=4,jsj=7,jxj=3,qkfp-,cxlhd-,pq=4,sls=5,pq=1,zftx-,zt-,tpnf=3,ksh-,tq-,flg=3,rzh=2,ft-,prs-,tmtnb=8,hf=8,kv=6,jz=1,qgz=4,vdsn=6,xc-,ps-,tz=3,sxht-,jp-,nj=1,lvx=6,tvr-,nqj-,bt=9,vcs-,rhd-,dp-,qq=4,shm-,bb=3,js-,fj-,cgln-,jz=7,rtg=5,zxk-,lr-,xd-,klmlv=6,kmtk=5,mb=6,pnrk=8,mb=4,dz=2,plm=3,bsflq-,pkc-,qd=6,rsvn-,cc-,tftg=1,kmlft-,dk=7,cp=1,rmgxs=8,ps=6,kmlft=1,vq-,ldc-,df=7,npcxkn-,mqjk-,zr-,szx=8,qmd-,sf=9,sqq=4,hs-,cm-,hh=1,klmlv=7,plfn=3,kp=6,zxvqk=4,nbc-,vpj-,zqbr-,pjr-,lrc-,kdb=7,zr-,djrhq-,cvfr=7,pjr-,dcp=8,dfv=4,snt=2,nms=9,hsmkv=5,vnqqfc=6,szx=2,vk=9,kmlft-,tdf-,gn=4,nst-,ldc-,dp-,rhd-,prs=4,lccj-,zg=9,bsflq=4,npcxkn-,dv-,hsmkv-,lrc=7,sqq=1,tvr-,tp-,fpx-,qhs-,cv-,jmtr-,gg=1,hr=9,rz=1,lfjj-,cg=8,qpm=4,vbsrn-,hd-,rc=8,dq-,qq=7,hnz-,mcq=1,dqz=2,kxf-,jz-,bxk=4,kbp-,cmb=5,nnpq-,pjr-,mxc-,cnbf=6,tqv-,tcmn=5,ssz=7,gz-,fpx-,nqg=6,bnh-,vdpj=1,gkcr=1,lr-,hfb-,qq-,cf-,jfsfp=8,pt-,crh=2,rmlm-,hkj-,snf-,jfsfp-,shqrb=5,mhrvl-,ps=3,dz-,crh-,lzn-,zsq=7,kr=2,qr=6,njz=1,hq=9,xkd-,pf=8,zc-,nkt=7,xrbt-,cbttmk-,cc=2,lt-,nbc-,sj=1,nk-,qfp-,rsg=8,xp=5,cnbf=4,nn=7,qpm-,dgz-,kzbcjm-,pnrk=1,jclfth=4,prf-,czc=2,zj=8,fjmc-,sdrk=7,tb=3,dscl-,vpj-,bb=2,bxk=3,pb=1,vdsn=5,rzq=7,grk=6,tx=9,zvt=2,kv-,fqz-,qmd=7,cg-,sjq-,zcjx=4,qkfp-,tnkx=3,gjx=7,skpk-,cb=9,vqzj=9,qtp=6,dgbzr-,grdn=2,sxht-,thm-,cpq-,pv=7,hp-,nmh-,rmgxs-,gfqclt-,fsxrqj-,rdfr-,vkq=2,fx-,jsj-,gfqclt-,zr=3,tp-,nst=8,thp-,hnz=5,xvz-,fx-,pnrk=9,dz=2,cgl=5,vpxxc-,hkj-,cgtd=4,qfp-,cl=8,hh=5,ptbr-,kv=8,lq-,hpp=3,kdb=7,pt=9,njz=5,vcv-,rzq-,kg-,pgz-,cp-,thcs-,qhs-,dp-,bb-,pgz-,bb=2,ssz-,zsq-,jxj=6,xrbt-,tp-,cnbf=3,gfgk=1,mjs-,xp-,th-,mkd=3,hvvmc=9,xdk=3,fsc=3,scq=4,pjr=3,mv-,dl-,tbtqj-,kv=3,lkqp=5,sdrk-,zqnp-,pjl=5,gjx=9,kk=8,mlzp=5,tdz=2,zj=3,xg=4,csmch=2,mkd=4,pv=9,nkt-,qb-,vtmxq-,rr=1,prf-,hgh-,nl-,pvz=3,sgh-,snf=6,dbblf-,ppzh=1,qb-,ds=9,nkt-,bnjjz=3,hvvmc-,kmtk-,mr-,rfzs-,ldc-,ds=1,mv-,np-,vdpj-,gt-,kbp-,pkc-,nzpbn=9,cfb=1,qmd-,bpc-,ptbr=2,cvjr-,zc=4,tq=4,kv-,pjr-,mkvv-,nh-,xdg=1,grk-,kjls=1,shf-,xmn=8,qtp-,vtmxq=5,zcjx=6,nn=6,fsxrqj-,qd-,xtvm-,jrl=9,ds-,djrhq-,cxlhd=7,dbblf=6,dmq=5,dqz=8,gnj-,kg=3,dmtdl=3,kzbcjm-,bnjjz-,dxts-,skpk=4,ptkrnb=4,rr-,vsxfqp-,xhsp-,tkd=3,vd-,bnjjz=1,tftg=9,nkp-,nk-,vkf=9,vn=4,hsz-,sq-,dtfj=8,prf-,grdn-,qf-,pfvqp=3,bgj=3,jclfth=6,rbs=3,bzfvl=3,vss=8,jmtr=4,xdk-,mbrs-,qkfp-,tt-,hjm-,bb-,zh=5,np=1,kdm=5,dk-,nst=4,jclfth=7,pjsvd=4,dthz-,zhzz-,cs=5,sq=6,xxsfxb=9,sljtvf-,cgtd-,mlzp-,prf=3,gjx-,ft-,bb-,zsq=5,slc=7,jl=1,hp=7,tbm=3,nj=3,ds-,pkc=1,szx=7,rsvn-,kdm-,lvx-,kdb=2,pvsb=1,dmq-,pkzff-,hvvmc=9,xq-,gpttz=4,cm-,dqz=5,qtl=1,xhsp=2,ldc-,ch=7,ps=6,ldb-,lccj-,tbl=7,qd-,dbblf-,pgz=8,zhpfgc-,dmtdl=7,zhzz=9,gz=5,zxk-,vkf=7,dv=9,llr=3,kfz-,hm=6,qx-,mkd=1,cx=9,tvttkp=5,rbs-,xdg=5,bsflq=6,sp-,ldc=3,ch-,htk=1,pjdrpt-,cb=8,fl=2,lnvkl=2,pl=4,pd=1,kv-,sqq-,kh=9,mkvv-,thp-,rbs-,mvd-,tbl=9,sqq-,mb=5,tdjzd=4,lzn=1,qpm=5,vn-,ppzh-,cbsmlt=4,dbblf-,njz-,sj=5,rt=3,kv=5,zcjx=7,gpttz=1,jrl-,htk-,mdx-,ttn-,rfzs=1,jmtr=7,zc-,tdjzd=5,jmb-,kxf-,dq-,cz-,vxf-,lxc=6,vkq-,gvh-,dv=7,dxts=8,ht-,zg=4,dmtdl-,grdn-,pjsvd=1,tdf-,jfd-,zjm=5,hkj=5,xmn-,pmkqk-,kbp=7,bk=5,xp=2,xdj-,bt-,hfb-,nkb-,rzq-,tb=3,ps-,njz=6,hpp=3,mr=9,xhsp-,dp-,jz=4,gfqclt-,vdjz=6,tqv=8,nzpbn-,bnh-,bnh-,shm=3,zsq-,zqm=6,zr=2,qglt-,dcp-,vpcz-,tdjzd-,scq-,nq-,pmkqk=8,cvjr-,ms=6,lqdd-,dl=5,mh=1,dq=6,bfbt-,rtg-,mvd=2,snf=9,xqbhnt=1,xkd=1,gd=2,ffzvk=1,dq-,vsmvd-,sh=5,vcs-,grs-,tq=8,mv-,nc=6,zxvqk=7,zhv=6,zsq=7,zj-,rnhrk-,tb=4,sjcf=5,pvjz=5,mdqz=9,ltlm=4,ms-,ft-,pl-,flg-,gkcr=7,fbm-,ft=2,rp=7,fhzj=7,sjq=4,xkd=5,zjm-,cm-,prf=4,ptkrnb-,tpnf-,lf-,gfq=7,bq-,vx=4,ft=2,hh=7,vqzj-,rt=5,ptkrnb-,dmmk-,ttn-,hq=3,bfbt=9,nmh-,hnz-,vfb=5,djrhq=6,hm=6,kk=4,hgh-,fdgp=9,tv=2,hfb=2,mb=6,xrbt-,tc-,dxts-,qkfp-,gfqclt=8,dl-,qglt-,nh=2,dnrx=2,vmnt=7,snt=1,hgh=5,fr-,fnd-,pq=8,lccj=4,pnrk-,dnrx-,qzs-,qgz=9,fbf=6,vpcz-,nh-,fnd=8,zhv-,nq=4,bq=1,mv-,scq-,dz=1,bmhf-,vpxxc=6,mqjk=4,xp=8,cm-,vd-,gxpr-,jqc-,fsc=9,th-,dj-,np-,jmb-,sp-,bmhf-,vxf=2,szx-,rrnz-,tpnf=1,vkf=2,ctm=9,lnvkl=7,dmmk-,nkt-,rfl=4,qgz-,cx=8,kmtk=9,rc=2,ch-,rmkb=5,vq-,tq-,hglng-,ltlm-,gfq=4,ggq=1,dvq=9,kxf-,xtvm=4,jqxl=7,bmn-,pbpb-,gvzx=4,lqdd=2,rz-,xt-,tpnf=5,tnkx=2,vcv-,ffzvk=6,zxvqk-,kv=9,dbblf-,th=5,pvjz-,nbds=6,qf=6,lccj=7,tlf-,rsg=3,vsmvd=7,nbds=9,bgd=7,sq-,qtl=1,qfp-,gd=3,drsx-,lc=4,gs-,kmlft=9,cx-,rmkb-,sv-,qb-,mkk=9,hlcpzb=1,fnd=7,xt-,mh-,vpcz=6,sf=8,pnrk-,ldc-,fpm-,nkt=7,gsp-,vpxxc-,xvz-,cvjr-,hpp=1,vjjfgc=6,vpj=4,lc=3,tdz=8,tvlqfg-,nkt=6,cb-,hlc=9,sxht-,lvx-,vbk-,rkv-,cpn-,tc=7,sx-,nmh-,fl-,zqm=1,dmq=3,np=9,rzh=9,qf=9,fx-,hs=9,kbp=6,mjs=9,vsmvd=7,ffsn-,gd-,lt=7,tp=2,xdj=5,rr-,zqm=4,ltlm-,mqjk-,lqgpv=4,vsxfqp=1,crg-,tdjzd=1,xq=8,gd=4,vk=3,ps=6,cv-,ldc-,gkcr-,lqdd=9,dv-,kr=3,lh=5,tz=3,bgj=3,gmpj-,ch=1,jxj=2,rbs=1,lvx-,sls=2,mdqz-,lr-,vkf-,zgk-,qr=4,qgz=7,th-,sdrk=8,bsflq-,cvjr-,tx=9,bhg-,lvx-,ptbr=9,tx=4,lfzf-,fsc-,kkgt-,sjq-,zvt-,mjqhbk=1,dscl-,rfl-,sxht-,vq=4,fsc-,sp-,th-,xmn-,vdjz-,xvz-,zvt-,ctm=2,vn=5,sf-,fsxrqj-,tcmn-,nqg-,gfq-,plm-,ltlm=1,fbm-,ltlm=2,fdtl=6,lvx=3,czc=9,dq=6,pjl-,jsj=3,ssz-,vbsrn=2,hvvmc=9,zhzz=1,vmnt-,hp=8,dmtdl-,rbs=1,dqz-,nkb=2,npcxkn=7,kh=4,vsxfqp=2,rc=4,gvzx=6,dsj=7,rzl-,vx=1,fgf=9,thcs=9,lp=5,sh-,sgh-,fl=5,rr-,fdgp=3,bnjjz=4,ppzh-,zlms=1,hfb-,gbvf-,ptk=9,ft=4,pvz-,vdjz=6,pv-,mdqz-,shm=3,ds=9,vpxxc-,fqz=7,rtg-,tp=8,pv-,lfzf-,sjq=3,kbp-,cfb=4,gmpj=3,rt-,csmch=9,nc-,sh=4,cgtd=5,phxjs-,dthz-,cs=7,zlms=9,bgj-,pln-,kg-,pfvqp-,zrbc=5,vx=2,dh-,nqg-,ddpml-,skpk=7,qpm=3,fj=8,sf=2,xdk=2,jsj-,zqm-,zhv-,rpmz=6,gsp-,mcq=4,lq=8,mn-,ds=6,cm-,xb-,zg=4,tbm=8,ddpml-,czc-,ppzh=3,xkd=3,zxk-,ctm=6,vjjfgc=1,dz-,fmqbk=3,pb-,thm=4,lfjj-,zsq-,gbvf=2,hb=5,ffsn-,zgb-,kg=6,vzt-,xxsfxb=4,jz-,cmb=6,rnhrk=6,vss-,hjm-,hlcpzb-,vsxfqp-,rhd-,plm-,gg=9,zvt=5,jqxl-,vbsrn=7,lbjp=5,xdg=8,hh=4,gjx-,vcv-,gdld-"
)

type Lens struct {
	label string
	value int
}

func main() {
	fmt.Println("Result 1:", sumHashes(strings.Split(day15, ",")))

	boxes := make([][]*Lens, 256)
	for _, cmd := range strings.Split(day15, ",") {
		applyCommand(boxes, cmd)
	}
	fmt.Println("Result 2:", valueBoxes(boxes))
}

func sumHashes(strings []string) (result int) {
	for _, s := range strings {
		result += int(hashStr(s))
	}
	return result
}

func hashStr(s string) (result byte) {
	for _, c := range s {
		result += byte(c)
		result *= 17
	}
	return result
}

func valueBoxes(boxes [][]*Lens) (result int) {
	for bi, box := range boxes {
		for li, lens := range box {
			result += (bi + 1) * (li + 1) * lens.value
		}
	}
	return result
}

func applyCommand(boxes [][]*Lens, str string) {
	if str[len(str)-1] == '-' {
		label := str[:len(str)-1]
		boxes[hashStr(label)] = slices.DeleteFunc(boxes[hashStr(label)], func(lens *Lens) bool {
			return lens.label == label
		})
		return
	}
	split := strings.Split(str, "=")
	label := split[0]
	value, err := strconv.Atoi(split[1])
	if err != nil {
		panic(err)
	}
	lens := &Lens{
		label: label,
		value: value,
	}
	if i := slices.IndexFunc(boxes[hashStr(label)], func(l *Lens) bool {
		return l.label == label
	}); i >= 0 {
		boxes[hashStr(label)][i] = lens
	} else {
		boxes[hashStr(label)] = append(boxes[hashStr(label)], lens)
	}
}

func (l *Lens) String() string {
	return fmt.Sprintf("[%v %d]", l.label, l.value)
}
