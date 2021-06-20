_base_ = './cascade_rcnn_r50_fpn_20e_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=6),
        mask_head=dict(num_classes=6)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ("badge", "person", "glove", "wrongglove", "operatingbar", "powerchecker")
data_root = 'data/gloves/'
data = dict(
    train=dict(
        img_prefix='',
        classes=classes,
        ann_file='data/gloves/annotations/instances_train2017.json'),
    val=dict(
        img_prefix='',
        classes=classes,
        ann_file='data/gloves/annotations/instances_val2017.json'),
    test=dict(
        img_prefix='',
        classes=classes,
        ann_file='data/gloves/annotations/instances_val2017.json'))

model = dict(
    type='CascadeRCNN',
    pretrained='open-mmlab://resnext101_64x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch'))
