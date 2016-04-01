#!/usr/bin/env python
#
# Copyright 2015-2016 Flavio Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Date, Integer, Text, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Index, DefaultClause
from sqlalchemy.dialects.postgres import TIMESTAMP

from firenado.util.sqlalchemy_util import Base


class PostBase(Base):

    __tablename__ = 'posts'

    id = Column('id', Integer(), primary_key=True)

    guid = Column('guid', String(255), nullable=False)

    content = Column('content', Text(), nullable=False)

    title = Column('title', Text(), nullable=False)

    excerpt = Column('excerpt', Text(), nullable=False)

    created = Column('created', TIMESTAMP(), nullable=False)

    updated = Column('updated', TIMESTAMP(), nullable=False)
