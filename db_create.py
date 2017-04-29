from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Nd(Base):
    __tablename__ = 'Nd'
    id = Column(Integer, primary_key=True)
    idx = Column(String(50))
    ro = Column(String(50))
    rb = Column(String(50))
    wo = Column(String(50))
    re = Column(String(50))
    we = Column(String(50))
    rq = Column(String(50))
    wq = Column(String(50))
    ure = Column(String(50))
    uwe = Column(String(50))
    urq = Column(String(50))
    uwq = Column(String(50))
    pre = Column(String(50))
    pwe = Column(String(50))
    pro = Column(String(50))
    pwo = Column(String(50))
    upload_id = Column(String(50))

    # email = Column(String(120), unique=True)
    # posts = relationship('Post', backref='author')

    
    def __repr__(self):
        return '<Nd {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}>'.format(self.idx, self.ro, self.rb, self.wo,
                                                                                  self.re, self.we, self.rq, self.wq,
                                                                                  self.ure, self.uwe, self.urq, self.uwq, 
                                                                                  self.pre, self.pwe, self.pro, self.pwo,
                                                                                  self.upload_id)

class Nm(Base):
    __tablename__ = 'Nm'
    id = Column(Integer, primary_key=True)
    idx = Column(String(50))
    ro = Column(String(50))
    wo = Column(String(50))
    rb = Column(String(50))
    wb = Column(String(50))
    re = Column(String(50))
    we = Column(String(50))
    rq = Column(String(50))
    wq = Column(String(50))
    ure = Column(String(50))
    uwe = Column(String(50))
    urq = Column(String(50))
    uwq = Column(String(50))
    pre = Column(String(50))
    pwe = Column(String(50))
    pro = Column(String(50))
    pwo = Column(String(50))
    upload_id = Column(String(50))

    # ['idx', 'id' 'ro', 'wo', 'rb', 'wb', 're', 'we', 'rq',
    #     'wq', 'ure', 'uwe', 'urq', 'uwq', 'pre', 'pwe', 'pro', 'pwo'] не ввел поле id !!!

    
    def __repr__(self):
        return '<Nm {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}>'.format(self.idx, self.ro, self.wo, self.rb, 
                                                                                  self.wb, self.re, self.we, self.rq, self.wq,
                                                                                  self.ure, self.uwe, self.urq, self.uwq, 
                                                                                  self.pre, self.pwe, self.pro, self.pwo,
                                                                                  self.upload_id)

class Nv(Base):
    __tablename__ = 'Nv'
    id = Column(Integer, primary_key=True)
    idx = Column(String(50))
    ctps = Column(String(50))
    ctrhs = Column(String(50))
    ctrhps = Column(String(50))
    ctds = Column(String(50))
    ctwfts = Column(String(50))
    ctwwts = Column(String(50))
    ctwfws = Column(String(50))
    ctwhs = Column(String(50))
    cv = Column(String(50))
    cm = Column(String(50))
    ctws = Column(String(50))
    ctrs = Column(String(50))
    ctr = Column(String(50))
    ctw = Column(String(50))
    ctp = Column(String(50))
    ctrh = Column(String(50))
    ctrhp = Column(String(50))
    ctd = Column(String(50))
    ctwft = Column(String(50))
    ctwwt = Column(String(50))
    ctwfw = Column(String(50))
    ctwfwsh = Column(String(50))
    ctwfwshs = Column(String(50))
    ctwh = Column(String(50))
    gwot = Column(String(50))
    gwo = Column(String(50))
    gws = Column(String(50))
    gwl = Column(String(50))
    ro = Column(String(50))
    wo = Column(String(50))
    wou= Column(String(50))
    rb = Column(String(50))
    wb = Column(String(50))
    rl = Column(String(50))
    wl = Column(String(50))
    rlw = Column(String(50))
    wlw = Column(String(50))
    xl = Column(String(50))


    # vdisk_perf_counters = ['idx', 'ctps', 'ctrhs', 'ctrhps', 'ctds', 'ctwfts', 
    #     'ctwwts', 'ctwfws', 'ctwhs', 'cv', 'cm', 'ctws', 'ctrs', 'ctr', 'ctw', 'ctp',
    #     'ctrh', 'ctrhp', 'ctd', 'ctwft', 'ctwwt', 'ctwfw', 'ctwfwsh', 'ctwfwshs',
    #     'ctwh', 'gwot', 'gwo', 'gws', 'gwl', 'id - НЕТ !!!', 'ro', 'wo', 'wou', 'rb', 'wb', 'rl',
    #     'wl', 'rlw', 'wlw', 'xl']  не ввел поле id !!!

            

    def __repr__(self):
        return '<Nv {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}>'.format(self.idx, self.ctps, self.ctrhs, self.ctrhps, self.ctds, 
                                                                                   self.ctwfts, self.ctwwts, self.ctwfws, self.ctwhs, self.cv,
                                                                                   self.cm, self.ctws, self.ctrs, self.ctr, self.ctw, self.ctp,
                                                                                   self.ctrh, self.ctrhp, self.ctd, self.ctwft, self.ctwwt, 
                                                                                   self.ctwfw, self.ctwfwsh, self.ctwfwshs, self.ctwh, self.gwot,
                                                                                   self.gwo, self.gws, self.gwl, self.ro, self.wo, self.wou, self.rb,
                                                                                   self.wb, self.rl,self.wl, self.rlw, self.wlw, self.xl)

if __name__ == "__main__":
    
    Base.metadata.create_all(bind=engine)

